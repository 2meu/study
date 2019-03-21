var apiKey ='AIzaSyBt3aTnFJz9zvryJq-tHe3wq7hNzjJtjK0';
var playlistId = 'PLScC8g4bqD45eu7f_keu6C-SJ31wxZip6';
var url = 'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&playlistId=' + playlistId + '&key=' + apiKey + '&maxResults=50';

function call(nextToken) {

  // 지금부터 XMLHttpRequest와 관련된 기능을 사용하겠습니다.
  var req = new XMLHttpRequest();
  // url에 해당되는 주소로 접속하고 싶어요.
  var pageToken = '';

  if (nextToken) {
    pageToken = '&pageToken=' + nextToken;
  }
  //  세번째 파라미터(생략 가능)는 요구가 비동기식(Asynchronous)으로 수행될 지를 결정합니다. 만약 이 파라미터가 true(기본값) 으로 설정된 경우에는 자바스크립트 함수가 지속적으로 수행될 수 있어 서버로부터 응답을 받기 전에도 유저와 페이지의 상호작용이 계속 진행됩니다. 이것이 AJAX 의 첫번째 A (Asynchronous : 비동기성) 입니다.
  //false로 설정된 경우 동기적으로 작동합니다. (send() 함수에서 서버로부터 응답이 올 때까지 기다림)역자 덧붙임
  req.open('GET', url + pageToken, true);

  // 위에서 생성한 httpRequest의 onreadystatechange property에 특정 함수 function(aEvt)를 할당하면
  // 요청에 대한 상태가 변화할 때 특정 함수 function(aEvt)가 불리게 됩니다.
  req.onreadystatechange = function (aEvt) {
    //XMLHttpRequest.DONE (상수 4로 정의되어 있습니다.) 라면, 서버로부터 모든 응답을 받았으며 이를 처리할 준비가 되었다는 것을 뜻합니다.
    if (req.readyState == 4) {
      // AJAX 요청이 정상적으로 처리되었는지 아닌지만을 검사하기 위해 응답 코드가 200 OK 인지 검사
      if (req.status == 200) {
        // http_request.responseText – 서버의 응답을 텍스트 문자열로 반환할 것이다.
        // text 형식이므로 JSON 형식으로 만들어주자
        var result = JSON.parse(req.responseText);
        var items = result.items;
        for (var i = 0; i < items.length; i++) {
          var vid = items[i].snippet.resourceId.videoId;
          var vurl = 'http://www.youtube.com/watch&v=' + vid;
          console.log(items[i].snippet.title + '\t' + vurl + '\t' + items[i].snippet.publishedAt);
        }
        if (result.nextPageToken) {
          call(result.nextPageToken);
        }
      } else {
        alert("Error loading page\n");
      }
    }
  };
  // 접속을 시작합니다.
  req.send(null);
}
call();
