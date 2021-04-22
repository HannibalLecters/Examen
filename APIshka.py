import cherrypy

Porno_Stars = {
    'Jonny Sins': {
        'id': '001',
        'username': 'Jonny_Big_Dick_28',
        'email': 'jonnysinsvkisku28@porn.cum',
        'department': 'Anal Department',
        'date_joined': '13.01.2004'
    },
    'Sasha Grey': {
        'id': '002',
        'username': 'Sasha_Grey_House',
        'email': 'sashagreyhouse13@porn.cum',
        'department': 'Cook Cum Pie',
        'date_joined': '15.06.2001'
    },
    'Ariana Marie': {
        'id': '003',
        'username': 'Anna_Maria_000',
        'email': 'arianafishmaster000@porn.cum',
        'department': 'Ass Accept',
        'date_joined': '27.02.2005'
    }
}

class Actors:
    def GET(self, name=None):
        if name == None:
            return ('All actors: %s' % Porno_Stars)
        elif name in Porno_Stars:
            actor = Porno_Stars[name]
            return ('Our actors: %s' % actor)
        else:
            return ('No actor with name %s' % name)
    exposed = True

# class Departments:
#     def GET(self, department=None):
#         list = []
#         if department == None:
#             for dep in Porno_Stars:
#                 list.append(dep.get('department'))
#             return ('All departments: %s' % list)
#         else:
#             for dep in Porno_Stars:
#                 if dep.get('department').find(department) != -1:
#                     list.append(dep.get('department'))
#             return list

if __name__ == '__main__':
    cherrypy.tree.mount(
        Actors(), '/api/pornostars', {
            '/':
                {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )
    # cherrypy.tree.mount(
    #     Departments(), '/api/department', {
    #         '/':
    #             {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    #     }
    # )

    cherrypy.engine.start()
    cherrypy.engine.block()


