PROVIDER=""

def driver_sqlite()->None:
    pass

def driver_s3_aliyun()->None:
    pass

def driver_s3_tencent()->None:
    pass

def driver_s3_aws()->None:
    pass

def main(provider:str)->None:
    if "aliyun" in provider:
        driver_s3_aliyun()
    elif "tencent" in provider:
        driver_s3_tencent()
    elif "aws" in provider:
        driver_s3_aws()
    else:
        pass

if __name__ == "__main__":
    main(PROVIDER)