let sttBtn = document.querySelector('.sttTrigger');
sttBtn.onclick = function(){
    document.querySelector('#modal').classList.remove('hide');
    setTimeout(sendSpeech(), 500);
}
let againBtn = document.querySelector('.againBtn');
againBtn.onclick = function(){
    setTimeout(sendSpeech(), 500);
}
let submitBtn = document.querySelector('.submitBtn');
submitBtn.onclick = function(){
    let context = document.querySelector('.output').innerText;
    document.querySelector('#modal').classList.add('hide');
    document.querySelector('.search input').value = context;
    document.querySelector('.output').innerText = "";
}

var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition;
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList;
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent;
var diagnosticPara = document.querySelector('.output');

function sendSpeech() {
  var recognition = new SpeechRecognition();
  var speechRecognitionList = new SpeechGrammarList();
  recognition.grammars = speechRecognitionList;
  recognition.lang = 'ko-KR';
  recognition.interimResults = false; // true: 중간 결과를 반환, false: 최종 결과만 반환
  recognition.continious = false; // true: 음성인식을 계속해서 수행, false: 음성인식을 한번만 수행
  recognition.maxAlternatives = 1;

  recognition.start();

  recognition.onresult = function(event) {
    var speechResult = event.results[0][0].transcript.toLowerCase();
    console.log('Confidence: ' + event.results[0][0].confidence);
    console.log('Speech Result: ' + speechResult);
    diagnosticPara.textContent = speechResult;
  }

  recognition.onaudiostart = function(event) {
      //Fired when the user agent has started to capture audio.
      console.log('SpeechRecognition.onaudiostart');

      document.querySelector('.status').style.transform = 'scale(120%)';
      setTimeout(function(){
        document.querySelector('.status').style.transform = 'scale(108%)';
      }, 200);
      setTimeout(function(){
        document.querySelector('.status').style.transform = 'scale(116%)';
      }, 400);
      setTimeout(function(){
        document.querySelector('.status').style.transform = 'scale(100%)';
      }, 600);
      setTimeout(function(){
        document.querySelector('.status').style.transform = 'scale(120%)';
      }, 800);
  }

  recognition.onaudioend = function(event) {
      //Fired when the user agent has finished capturing audio.
      console.log('SpeechRecognition.onaudioend');
  }

  recognition.onend = function(event) {
      //Fired when the speech recognition service has disconnected.
      console.log('SpeechRecognition.onend');
  }

  recognition.onnomatch = function(event) {
      //Fired when the speech recognition service returns a final result with no significant recognition. This may involve some degree of recognition, which doesn't meet or exceed the confidence threshold.
      console.log('SpeechRecognition.onnomatch');
  }

  recognition.onsoundstart = function(event) {
      //Fired when any sound — recognisable speech or not — has been detected.
      console.log('SpeechRecognition.onsoundstart');
  }

  recognition.onsoundend = function(event) {
      //Fired when any sound — recognisable speech or not — has stopped being detected.
      console.log('SpeechRecognition.onsoundend');

      document.querySelector('.status').style.transform = 'scale(90%)';
  }

  recognition.onspeechstart = function (event) {
      //Fired when sound that is recognised by the speech recognition service as speech has been detected.
      console.log('SpeechRecognition.onspeechstart');
  }
  recognition.onstart = function(event) {
      //Fired when the speech recognition service has begun listening to incoming audio with intent to recognize grammars associated with the current SpeechRecognition.
      console.log('SpeechRecognition.onstart');
  }
}
