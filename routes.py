class AcknowledgeRoute(object):
    path = '/acknowledge'
    endpoint = 'acknowledge'

    def handle(self):
        return 'OK'
