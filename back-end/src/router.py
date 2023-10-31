

class Router:

    def run(app):
        
        print("*************[Dest pê  dike!!]*************")
        
        #UserControllers Routes..
        from routes.CheckCepRouter import CheckCepRouter
        app.register_blueprint(CheckCepRouter, url_prefix='/api')

        #post
        # from application.routes.PostRouter import PostRouter
        # app.register_blueprint(PostRouter,url_prefix="/posts")

        # #Index Page!
        # from application.routes.IndexRouter import IndexRouter
        # app.register_blueprint(IndexRouter, url_prefix="/")