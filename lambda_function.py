import json

def lambda_handler(event, context):
    # TODO implement
    
    print("these changes should be reflected in lambda after commit")
    print("second push")
    #print("push from branch2 to master")
    return {"status":200, "body":json.dumps("hello from lambda and github,demo for push to master bramch")}

    
    

