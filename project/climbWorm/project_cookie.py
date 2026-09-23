
import requests

url = "https://www.lagou.com/wn/jobs?cl=false&fromSearch=true&kd=python&u_atoken=e41d883e1cf4afd1b5f2f53e84919cbe&u_asig=ac11000117869691715872430e0135"

headers = {
    #模拟浏览器
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36", 
    "Host": "www.lagou.com",
    "Referer": "https://www.lagou.com/wn/jobs?cl=false&fromSearch=true&kd=python",
    "Cookie": "ssxmod_itna=1-iqmxBQG=0=0QKAKDQG0D2ipbGOnxGQfe4DXDUqAQD2DIMq7=GFYDCEh94YvNbLPwegb7YR4dDopdHNDlOx4oDSxD67DK4GTm_=0GmzQmDgEPveFmubXCemBW_HvFbQ0oiIo35uGT9U6Dys/jDT42vksa4DHxi8DBFqp7roDeeFDCeDQxirDD4DAioD=xDrD0bvDYPPsG4DXgAfDGPeTD0dc3rvDQP3DY5wA04AbDDz8ArigDGrDmbvmRAXAD07DiHqm8hP14G1jD0HiDUUDDHBwdxfmIZ9=unpUS3DvxDkAnoDogYcnDSAmfOmGDchGmYrKGei0o=BYg7DbAxnE5rDtKExb7oSYbb7b4rb5QmsxDiE0blpXQGgi_BrXMEN/rqbm0xmqgWKCRmXnGPiGeYIhGKbQrsDehmIzfwPAipivz4hTt0pQi40ez3I83hzbYcDPclppewXzixD; ssxmod_itna2=1-iqmxBQG=0=0QKAKDQG0D2ipbGOnxGQfe4DXDUqAQD2DIMq7=GFYDCEh94YvNbLPwegb7YR4dDopd5oDicqRGCiji8GeYDFhiwC76DafPDlpDMjj=8Yt6Od509i_7yIsDHz97sXdIGgR2o9DIcaqwcpzA=9W/PTq8r0Yux240hKx_Pu4/rGeD42efr0G2QipgAItI=0G=GgwuGPefaEPb0vPFGaOqQIwinPeKApxgQ8Ie7rOf8GLKYyQmFDsuCMQNIFITaHpxSY_KbZnVbZAIpQcqvYCqmojNtkIdMvhOtAfzvp6M4rIMLLy4HQKIybGUCeZKuARq1SnISwHKDxXR7Qi6AvC_qCBuRGT4YqFUaq85_D7V3wzGu4G7jFitl5E0IXKizI7IFipnq9mqxDc1nb48iVjFv0_4jHkYA8_xqdnbrEbcIOiubZrk9EVWaQbiOiPomDo4d75dob0DS2N4bilrRR24/3CoLeeD; acw_tc=ac11000117869691715872430e013501502eb29e0f8f145899a2967cc8010d; _c_WBKFRo=nJzRe3zMYUc5jthb2pUv57Wue4jXhPYsU9qee8mi; _nb_ioWEgULi="
}

# resp1 = requests.get(url=url, headers=headers)

resp = requests.get(url=url, headers=headers)
print(resp.text)