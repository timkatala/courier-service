from django.db.models import Lookup
from django.contrib.postgres.fields import ArrayField


class HasIntersection(Lookup):
    lookup_name = 'has_intersection'

    def as_sql(self, compiler, connection):
        # The left-hand-side (lhs) in the query's WHERE clause. It consists
        # of your app name and field name. e.g. '"myapp"."scheduled"'
        # In this case, the left-hand-side has no params.
        lhs, lhs_params = self.process_lhs(compiler, connection)

        # The right-hand-side (rhs) + its params will define the input used
        # in sthe query's WHERE clause. At this point, the rhs_params will
        # be a datetime object, e.g.: datetime(2015, 10, 18, 0, 0, tzinfo=)
        rhs, rhs_params = self.process_rhs(compiler, connection)

        # Both PostgreSQL and MySQL have a DATE function that lets us query
        # by date. The where clause in the generated SQL will look something
        # like, WHERE DATE(scheduled) = '2015-10-18'
        params = lhs_params + rhs_params
        return 'has_intersection(%s, %s) = true' % (lhs, rhs), params
