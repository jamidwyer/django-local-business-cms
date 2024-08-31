import graphene

import businesses.schema as businesses_app

class Query(businesses_app.schema.Query, graphene.ObjectType):
    # Inherits all classes and methods from app-specific queries
    pass


schema = graphene.Schema(query=Query,)
