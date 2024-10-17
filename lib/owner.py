from __init__ import CONN, CURSOR
import ipdb

class Owner():

  def __init__(self, name, id=None):
    self.name = name
    self.id = id

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    self._name = name

  def adopt_pet(self, pet):
    pet.owner_id = self.id
    pet.save()

  def pets(self):
    from pet import Pet
    sql = '''
      SELECT * FROM pets
      WHERE pets.owner_id = ?
    '''

    rows = CURSOR.execute(sql, (self.id,))
    return [Pet.create_by_row(row) for row in rows]

  @classmethod
  def create_table(cls):
    sql = '''
      CREATE TABLE IF NOT EXISTS owners (
        id INTEGER PRIMARY KEY,
        name TEXT
      );
    '''

    CURSOR.execute(sql)

  @classmethod
  def drop_table(cls):
    sql = '''
      DROP TABLE owners;
    '''

    CURSOR.execute(sql)   

  @classmethod
  def create(cls, name):
    owner = Owner(name=name)
    owner.save()
    return owner
  
  @classmethod
  def find_by_id(cls, id):
    sql='''
      SELECT * FROM owners
      WHERE id = ?;
    '''

    row = CURSOR.execute(sql, (id,)).fetchone()
    if row:
      return Owner.create_by_row(row)
  
  @classmethod
  def all(cls):
    sql = '''
      SELECT * FROM owners;
    '''

    owners = CURSOR.execute(sql).fetchall()

    return [Owner.create_by_row(row) for row in owners]
  
  @classmethod
  def create_by_row(cls, row):
    return Owner(id=row[0], name=row[1])

  @classmethod
  def delete_all(cls):
    for owner in cls.all():
      owner.delete()

  def save(self):
    if not self.id:
      sql = '''
        INSERT INTO owners (name) VALUES (?)
      '''

      CURSOR.execute(sql, (self.name,))
      CONN.commit()
      sql = '''
        SELECT id FROM owners ORDER BY id DESC LIMIT 1
      '''
      self.id = CURSOR.execute(sql).fetchall()[0][0]

    else:
      sql = '''
        UPDATE owners SET name = ?
        WHERE id = ?
      '''

      CURSOR.execute(sql, (self.name, self.id))
      CONN.commit()

  def delete(self):
    sql = "DELETE FROM owners WHERE id = ?"
    CURSOR.execute(sql, (self.id,))
    CONN.commit()

  def __repr__(self):
    return f'<Owner id={self.id} name="{self.name}">'
