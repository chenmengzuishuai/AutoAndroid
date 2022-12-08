import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.nlp.v20190408 import nlp_client, models




def tencentchat(question):
    try:
        cred = credential.Credential(SECRETID, SECRETKEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "nlp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = nlp_client.NlpClient(cred, "ap-guangzhou", clientProfile)

        req = models.ChatBotRequest()
        params = {
            "Action":"ChatBot",
            "Version":"2019-04-08",
            "Region":"ap-guangzhou",
            "Query":question,

        }
        req.from_json_string(json.dumps(params))

        resp = client.ChatBot(req)
        replyStr = resp.to_json_string()
        replyStr = json.loads(replyStr)
        replyStr = replyStr["Reply"]
        if "腾讯" in replyStr:
            replyStr.replace("腾讯", "")
        if "小龙女" in replyStr:
            replyStr = "小芸"
        return replyStr
    except TencentCloudSDKException as err:
        print(err)



if __name__ == "__main__":
    print(tencentchat("你在哪里"))
