# VoyageManagementSystem

Use AWS CloudFormation to deploy the following steps:

Define an AWS::ApiGateway::RestApi resource to create the API Gateway.
Define an AWS::ApiGateway::ApiKey resource to create the API key and attach it to the API Gateway.
Define an AWS::ApiGateway::Resource resource to create a resource for the POST method.
Define an AWS::ApiGateway::Method resource for the POST method and specify its integration with a Lambda function using AWS::ApiGateway::Method#Integration.
Define an AWS::ApiGateway::Resource resource to create a resource for the GET method.
Define an AWS::ApiGateway::Method resource for the GET method and specify its integration with a Lambda function using AWS::ApiGateway::Method#Integration.
Define an AWS::DynamoDB::Table resource to create the database table.
Define an AWS::Lambda::Function resource for the Lambda function and specify its handler to point to the appropriate Python file.
Define an AWS::ApiGateway::UsagePlan Control, Monitor and Track API usage using UsagePlan
Define an AWS::ApiGateway::UsagePlanKey grant clients (users/applications) access to APIs which are deployed using API gateways
Note: Provide any necessary configuration properties for each resource, such as the API Gateway's base path or the DynamoDB table's attribute definitions.
