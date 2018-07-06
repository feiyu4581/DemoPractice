from app import create_app
from utils.route import register_route
import config

app = create_app()

register_route(app)

if __name__ == '__main__':
    app.run(host=config.HOST,
            port=config.PORT,
            debug=config.DEBUG,
            workers=config.WORKERS)
