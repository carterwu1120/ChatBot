from utils.env_reader import EnvData

class LlmApi:
    """
    base class of all Apis
    """
    role_description = ("You are an English tutor. You have two job. "
                        "First of all, <revise> revise my sentence or grammar </revise>. Please output the result in <revise> </revise> tags.\n"
                        "Secondly, </conversation> please continue the conversation </conversation>. Please output the result in <conversation> </conversation> tags.\n")
    envdata = EnvData()
