from models import engine

if __name__ == '__main__':
    from models import Base
    Base.metadata.create_all(engine)


    #  |-- Pipfile
    #  |-- Pipfile.lock
    #  |-- README.md
    #  |-- .venv
    #  |-- lib
    #     |-- db
    #         |-- migrations
    #             |-- versions
    #             |-- env.py
    #             |-- README
    #             |-- script.py.mako
    #         |-- alembic.ini  
    #         |-- budget_cli.py
    #         |-- database.py
    #         |-- main.py
    #         |-- models.py 
    #         |-- seed.py
    #         |-- budget_planner.db
    # |-- debug.py 
    # |-- helpers.py