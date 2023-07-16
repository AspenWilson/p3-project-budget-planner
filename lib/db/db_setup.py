from models import engine

if __name__ == '__main__':
    from models import Base
    Base.metadata.create_all(engine)


    # |-- Pipfile
    # |-- Pipfile.lock
    # |-- README.md 
    # |-- lib
    #     |-- db
    #         |-- alembic.ini  
    #         |-- budget_cli.py
    #         |-- db_setup.py
    #         |-- main.py
    #         |-- models.py 
    #         |-- seed.py