class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == "user":
            return "users"
        elif model._meta.db_table == "order":
            return "orders"
        elif model._meta.db_table == "product":
            return "products"
        return "default"

    def db_for_write(self, model, **hints):
        return self.db_for_read(model, **hints)

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
