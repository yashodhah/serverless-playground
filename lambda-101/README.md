* Exporting variables

API_URL=$(aws cloudformation describe-stacks --stack-name sam-app --query 'Stacks[0].Outputs[?OutputKey==`HelloWorldApi`].OutputValue' --output text)
LAMBDA_ARN=$(aws cloudformation describe-stacks --stack-name sam-app --query 'Stacks[0].Outputs[?OutputKey==`HelloWorldFunction`].OutputValue' --output text)
echo API_URL=$API_URL
echo LAMBDA_ARN=$LAMBDA_ARN


* Artilery Testing

  API_URL=$(aws cloudformation describe-stacks --stack-name sam-app --query 'Stacks[0].Outputs[?OutputKey==`HelloWorldApi`].OutputValue' --output text)

  artillery run --target $API_URL loadtest-canary.yaml
