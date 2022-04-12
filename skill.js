const Alexa = require('ask-sdk-core');
var http = require('http');

const HelloWorldIntentHandler = {
    canHandle(handlerInput) {
        return Alexa.getRequestType(handlerInput.requestEnvelope) === 'LaunchRequest' 
            || Alexa.getRequestType(handlerInput.requestEnvelope) === 'IntentRequest'
            && Alexa.getIntentName(handlerInput.requestEnvelope) === 'HelloWorldIntent';
    },
      async handle(handlerInput) {
        let speakOutput = "Default message"  
        const response = await httpCall();
        
        console.log(response);
        speakOutput = "OK";
        return handlerInput
            .responseBuilder
            .speak(speakOutput)
            .getResponse();
        }
};

function httpCall() {
  return new Promise(((resolve, reject) => {
    var options = {
        host: '192.168.X.XXX',
        port: 8081,
        path: '/zeroconf/switch',
        method: 'POST',
        json: {"deviceid":"","data":{"switch":"on"}}
    };
    
    const request = http.request(options, (response) => {
      response.setEncoding('utf8');
      let returnData = '';

      response.on('data', (chunk) => {
        returnData += chunk;
      });

      response.on('end', () => {
        resolve(JSON.parse(returnData));
      });

      response.on('error', (error) => {
        reject(error);
      });
    });
    request.end();
  }));
}