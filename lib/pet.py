from __init__ import CONN, CURSOR

import ipdb

class Pet():

  def __init__(self, name, species, owner_id=None, id=None):
    self.name = name
    self.species = species
    self.owner_id = owner_id
    self.id = id

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, name):
    self._name = name

  def owner(self):
    from owner import Owner
    sql = '''
      SELECT * FROM owners
      WHERE id = ?
    '''
    row = CURSOR.execute(sql, (self.owner_id,)).fetchone()
    if row:
      return Owner.create_by_row(row)

  @property
  def species(self):
    return self._species

  @species.setter
  def species(self, species):
     self._species = species

  @classmethod
  def create_table(cls):
    sql = '''
      CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT,
        owner_id INTEGER DEFAULT NULL
      );
    '''

    CURSOR.execute(sql)

  @classmethod
  def drop_table(cls):
    sql = '''
      DROP TABLE pets;
    '''

    CURSOR.execute(sql)   

  @classmethod
  def create(cls, name, species, owner_id=None):
    pet = Pet(name=name, species=species, owner_id=owner_id)
    pet.save()
    return pet
  
  @classmethod
  def find_by_id(cls, id):
    sql='''
      SELECT * FROM pets
      WHERE id = ?;
    '''

    row = CURSOR.execute(sql, (id,)).fetchone()
    if row:
      return Pet.create_by_row(row)
  
  @classmethod
  def all(cls):
    sql = '''
      SELECT * FROM pets;
    '''

    pets = CURSOR.execute(sql).fetchall()

    return [Pet.create_by_row(row) for row in pets]
  
  @classmethod
  def unadopted_pets(cls):
    sql = '''
      SELECT * FROM pets WHERE NOT owner_id NOT NULL;
    '''

    pets = CURSOR.execute(sql).fetchall()
    return [Pet.create_by_row(row) for row in pets]
  
  @classmethod
  def create_by_row(cls, row):
    return Pet(id=row[0], name=row[1], species=row[2], owner_id=row[3])

  @classmethod
  def delete_all(cls):
    for pet in cls.all():
      pet.delete()

  def save(self):
    if not self.id:
      sql = '''
        INSERT INTO pets (name, species, owner_id) VALUES (?, ?, ?)
      '''

      CURSOR.execute(sql, (self.name, self.species, self.owner_id))
      CONN.commit()
      sql = '''
        SELECT id FROM pets ORDER BY id DESC LIMIT 1
      '''
      self.id = CURSOR.execute(sql).fetchall()[0][0]

    else:
      sql = '''
        UPDATE pets SET name = ?, species = ?, owner_id = ?
        WHERE id = ?
      '''

      CURSOR.execute(sql, (self.name, self.species, self.owner_id, self.id))
      CONN.commit()

  def delete(self):
    sql = "DELETE FROM pets WHERE id = ?"
    CURSOR.execute(sql, (self.id,))
    CONN.commit()

  def adopt_owner(self, owner):
    self.owner_id = owner.id
    self.save()

  def unadopt(self):
    sql = '''
      UPDATE pets SET owner_id = NULL WHERE id = ?
    '''

    CURSOR.execute(sql, (self.id,))
    CONN.commit()

  def __repr__(self):
    return f'<Pet id={self.id} name="{self.name}" species="{self.species}" owner_id={self.owner_id}>'
