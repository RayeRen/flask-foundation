from app.models import db, User


def configure_commands(app):
    @app.cli.command
    def createdb():
        """ Creates a database with all of the tables defined in
            your SQLAlchemy models
        """
        db.create_all()
