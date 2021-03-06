# ModelBase

The base class used when creating the declarative base.

Can be used to easily create your own declarative base without having to use a `Manager` instance:

```python
# in project/core.py
from alchy import ModelBase, make_declarative_base

class Base(ModelBase):
    # augument the ModelBase with super powers

Model = make_declarative_base(Base=Base)
```

```python
# in project/models/user.py
from project.core import Model

class User(Model):
    # define declarative User model
```

## Instance Methods

### \_\_init\_\_()

Proxy to [ModelBase.update()](#update).

```python
ModelBase(*args, **kargs)

Model(data_dict)
Model(**data_dict)
Model(data_dict, strict=True)
```

### update()

Update a model instance using a single `dict` or via keyword arguments. Optionally, restrict updatable fields using `strict=True`. If model instance contains sequence values (e.g. relationships), then those values will be updated too via nested calls to `model.relationship.update(data_dict['relationship'])`.

```python
ModelBase.update(data_dict=None, strict=False, **kargs)

model.update(data_dict)
model.update(**data_dict)
model.udpate(data_dict, strict=True)
```

### to_dict()

Convert model instance to raw `dict`. Optionally, refresh instance if `dict` is empty using `refresh_on_empty=True`.

```python
ModelBase.to_dict(refresh_on_empty=True)

model.to_dict()
```

This method fetches state from `model.__dict__` while filtering keys on valid model descriptors (i.e. internal state values such as `_sa*` are ignored). It is assumed that `__dict__` will contain all database values that should be serialize. Thus, any relationships that need to be serialize but are lazy loaded by default will need to be pre-loaded before calling `to_dict()`. The [Query](query.md) class provides first-class access to SQLAlchemy's Load API which can be useful in these situations.

### flush()

Equivalent to `db.session.flush(model)`.

Requires that model was previously added/loaded by session.

```python
model.flush()
```

### save()

Equivalent to `db.session.add(model)`.

Requires that model was previously added/loaded by session.

```python
model.save()
```

### delete()

Equivalent to `db.session.delete(model)`.

Requires that model was previously added/loaded by session.

```python
model.delete()
```

### expire()

Equivalent to `db.session.expire(model)`.

Requires that model was previously added/loaded by session.

```python
model.expire()
```

`chainable`

### refresh()

Equivalent to `db.session.refresh(model)`.

Requires that model was previously added/loaded by session.

```python
model.refresh()
```

`chainable`

### expunge()

Equivalent to `db.session.expunge(model)`.

Requires that model was previously added/loaded by session.

```python
model.expunge()
```

`chainable`

## Instance Properties

### session

Proxy to `orm.object_session(model)`.

```python
model.session
```

### strict_update_fields

Returns updatable fields when `model.update(..., strict=True)` is called.

Default returns [model.columns](#columns).

Override to implement custom updatable fields:

```python
MyModelBase(ModelBase):
	@property
	def strict_update_fields(self):
		return ['field1', 'field2']
```

## Class Methods

### get()

Equivalent to `Model.query.get()` which is equivalent to `db.session.query(Model).get()`.

```python
Model.get(1)
```

### get_by()

Equivalent to `Model.query.filter_by().first()` which is equivalent to `db.session.query(Model).filter_by().first()`.

```python
Model.get_by(first='foo', last='bar')
```

### advanced_search()

Map the given search dict to the field/functions defined in [Model.\_\_advanced_search\_\_](#9595advanced_search9595) and AND together returning a query filter.

```python
Model.advanced_search(search_dict)

model.advanced_search({'field1': 'search1', 'field2': 'search2'})
```

### simple_search()

Pass the given search string to each function in [Model.\_\_simple_search\_\_](#9595simple_search9595) and AND together returning a query filter.

```python
Model.simple_search(search_string)

model.simple_search('search')
```

## Class Properties

### query

Query property which provides a proxy to `db.session.query.join(Model)` via `Model.query`.

```python
records = Model.query.all()
filtered = Model.query.join(Related).filter(Model.field1==value1, Related.field2>value2).all()
```

The query class used to instantiate `query` can be set using [Model.query_class](#query_class).

This interface is inspired by [Flask-SQLAlchemy](http://pythonhosted.org/Flask-SQLAlchemy/api.html?highlight=query#flask.ext.sqlalchemy.Model).

## Class/Instance Properties

### primary_key

Return Model's primary key(s) as `Column` objects. If there's only a single primary key, then that column is returned, otherwise, a tuple of columns is returned.

### attrs

Return Model's attrs as list of strings.

### descriptors

Return Model's ORM descriptors as list of strings.

### relationships

Return Model's relationships as list of strings.

### column_attrs

Return Model's columns as list of attributes.

### columns

Return Model's columns as list of strings.

## Class Configuration

### query_class

The query class to use when `Model.query` is accessed.

### \_\_events\_\_

Define event listeners on Model without using event decorators. For more details, see [Events](events.md) section.

**NOTE:** The final value of `Model.__events__` will contain an aggregate of the events defined directly on `__events__` and the events defined via event decorators.

### \_\_advanced_search\_\_

Enable [Model.advanced_search()](#advanced_search) by assigning a dict of functions that accept a value and return a query filter. The keys of the dict map the input keys of the search dict used in [Model.advanced_search()](#advanced_search).

```python
class MyModel(Model):
    __advanced_search__ = {
        'field1': lambda value: MyModel.field1.like('%{0}%'.format(value)),
        'prefix_field2': lambda value: MyModel.field2.like('%{0}%'.format(value)),
        'min_field3': lambda value: MyModel.field3 >= value,
        'max_field3': lambda value: MyModel.field2 <= value
    }

MyModel.advanced_search({'field1': 'search1', 'prefix_field2': 'search2', min_field3: 42})
```

### \_\_simple_search\_\_

Enable [Model.simple_search()](#simple_search) by assigning a dict of functions that accept a value and return a query filter. The keys of the dict are essentially irrelevant. They are used to keep the definition syntax consistent with [Model.__advanced_search__](#9595advanced_search9595).

```python
class MyModel(Model):
    __simple_search__ = {
        'field1': lambda value: MyModel.field1.like('%{0}%'.format(value)),
        'prefix_field2': lambda value: MyModel.field2.like('%{0}%'.format(value))
    }

MyModel.simple_search('search')
```
