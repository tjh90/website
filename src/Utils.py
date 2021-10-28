def isMobile(request):
    '''
    Determine if the request was sent by a mobile agent.

    @param request the request
    '''

    agent = request.user_agent.string.lower()
    for keyword in ['android', 'iphone', 'mobile']:
        if keyword in agent:
            return True

    return False
