from models import engine

if __name__ == '__main__':
    from models import Base
    Base.metadata.create_all(engine)
