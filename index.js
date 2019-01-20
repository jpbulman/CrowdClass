function makeApiCall() {
    var params = {
      // The ID of the spreadsheet to update.
      spreadsheetId: '1_Up8C6sKiGnA5VsY-6MMgI60MLpu7EHM6r1h7HIPx54',  // TODO: Update placeholder value.

      // The A1 notation of the values to update.
      range: 'C1',  // TODO: Update placeholder value.

      // How the input data should be interpreted.
      valueInputOption: 'RAW',  // TODO: Update placeholder value.
    };

    var valueRangeBody = {"values":[[1]]};

    var request = gapi.client.sheets.spreadsheets.values.update(params, valueRangeBody);
    request.then(function(response) {
      // TODO: Change code below to process the `response` object:
      console.log(response.result);
    }, function(reason) {
      console.error('error: ' + reason.result.error.message);
    });
  }

  function initClient() {
    var API_KEY = 'AIzaSyC6y1KR1gmGdpPpJqAZSVXx-TkNEwG2lUw';  // TODO: Update placeholder with desired API key.

    var CLIENT_ID = '164150838733-30m1b86or9d5s6e8oac1t5bu0t7s6elk.apps.googleusercontent.com';  // TODO: Update placeholder with desired client ID.

    // TODO: Authorize using one of the following scopes:
    //   'https://www.googleapis.com/auth/drive'
    //   'https://www.googleapis.com/auth/drive.file'
    //   'https://www.googleapis.com/auth/spreadsheets'
    var SCOPE = 'https://www.googleapis.com/auth/spreadsheets.readonly';

    gapi.client.init({
      'apiKey': API_KEY,
      'clientId': CLIENT_ID,
      'scope': SCOPE,
      'discoveryDocs': ['https://sheets.googleapis.com/$discovery/rest?version=v4'],
    }).then(function() {
      gapi.auth2.getAuthInstance().isSignedIn.listen(updateSignInStatus);
      updateSignInStatus(gapi.auth2.getAuthInstance().isSignedIn.get());
    });
  }

  function handleClientLoad() {
    gapi.load('client:auth2', initClient);
  }

  function updateSignInStatus(isSignedIn) {
    if (isSignedIn) {
      makeApiReadCall();
    }
  }

  function handleSignInClick(event) {
    gapi.auth2.getAuthInstance().signIn();
  }

  function handleSignOutClick(event) {
    gapi.auth2.getAuthInstance().signOut();
  }

  var lou = []
  function makeApiReadCall() {
    var params = {
      // The ID of the spreadsheet to retrieve data from.
      spreadsheetId: '1_Up8C6sKiGnA5VsY-6MMgI60MLpu7EHM6r1h7HIPx54',  // TODO: Update placeholder value.

      // The A1 notation of the values to retrieve.
      range: 'A1:A500',  // TODO: Update placeholder value.

    //   // How values should be represented in the output.
    //   // The default render option is ValueRenderOption.FORMATTED_VALUE.
    //   valueRenderOption: 'RAW',  // TODO: Update placeholder value.

    //   // How dates, times, and durations should be represented in the output.
    //   // This is ignored if value_render_option is
    //   // FORMATTED_VALUE.
    //   // The default dateTime render option is [DateTimeRenderOption.SERIAL_NUMBER].
    //   dateTimeRenderOption: 'FORMATTED_VALUE',  // TODO: Update placeholder value.
    };

    var request = gapi.client.sheets.spreadsheets.values.get(params);
    request.then(function(response) {
      // TODO: Change code below to process the `response` object:
      console.log(response.result);
      lou = response.result.values
      console.log(lou)
    }, function(reason) {
      console.error('error: ' + reason.result.error.message);
    });
  }

function setVal(){

    SCOPES="https://www.googleapis.com/auth/spreadsheets"
    handleClientLoad()
    // var vals = [1,2,3,4,5]
    // var params = {
    //     spreadsheetId: "1_Up8C6sKiGnA5VsY-6MMgI60MLpu7EHM6r1h7HIPx54",
    //      range: "C1:C5",
    //      valueInputOption: 'RAW',
    // }
    // var valueRangeBody = {"values": vals};
    //   var request = gapi.client.sheets.spreadsheets.values.update(params,valueRangeBody)
    //   request.then(function(response) {
    //     var result = response.result;
    //     console.log(`${result.updatedCells} cells updated.`);
    //   });

    var params = {
        // The ID of the spreadsheet to update.
        spreadsheetId: '1_Up8C6sKiGnA5VsY-6MMgI60MLpu7EHM6r1h7HIPx54',  // TODO: Update placeholder value.

        // The A1 notation of the values to update.
        range: 'C1',  // TODO: Update placeholder value.

        // How the input data should be interpreted.
        valueInputOption: 'RAW',  // TODO: Update placeholder value.
      };

      var valueRangeBody = {
        "values" : [[1]]
      };

      var request = gapi.client.sheets.spreadsheets.values.update(params, valueRangeBody);
      request.then(function(response) {
        // TODO: Change code below to process the `response` object:
        console.log(response.result);
      }, function(reason) {
        console.error('error: ' + reason.result.error.message);
      });

}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

var q1IsRight = false;
var qIsCC = false;

async function update(){
    await sleep(1500);
    var randCook = Math.floor((Math.random() * 400) + 0);

    var randNext = Math.floor((Math.random() * 400) + 0);

    if(Math.abs(lou[randCook][1])==10 && Math.abs(lou[randNext][1])==10){
        var rand = Math.floor((Math.random() * 2) + 1);

        if(rand==1){
            while(Math.abs(lou[randNext][1])==10){
                randNext = Math.floor((Math.random() * 400) + 0);
            }
            q1IsRight=false;
        }
        else{
            while(Math.abs(lou[randCook][1])==10){
                randCook = Math.floor((Math.random() * 400) + 0);
            }
            q1IsRight=true;
        }
    }
    else if(Math.abs(lou[randCook][1])==0 && Math.abs(lou[randNext][1])==0){
        var rand = Math.floor((Math.random() * 2) + 1);

        if(rand==1){
            while(Math.abs(lou[randNext][1])!=10){
                randNext = Math.floor((Math.random() * 400) + 0);
            }
            q1IsRight=false;
        }
        else{
            while(Math.abs(lou[randCook][1])!=10){
                randCook = Math.floor((Math.random() * 400) + 0);
            }
            q1IsRight=true;
        }
    }

    if(lou[randCook][1]==10 || lou[randNext][1]==10){
        qIsCC=true;
    }
    else{
        qIsCC=false;
    }

    // if(Math.abs(lou[randNext][1])==10){
    //     while(Math.abs(lou[randNext][1])==10){
    //         randNext = Math.floor((Math.random() * 400) + 0);
    //     }
    // }
    // else{
    //     while(Math.abs(lou[randNext][1])!=10){
    //         randNext = Math.floor((Math.random() * 400) + 0);
    //     }
    // }

    // if(Math.abs(lou[randCook][1])==10){
    //     q1IsRight = true;
    //     if(lou[randCook][1]==10){
    //         qIsCC = true;
    //     }
    //     else{
    //         qIsCC = false;
    //     }
    // }
    // else{
    //     q1IsRight = false;
    //     if(lou[randNext][1]==10){
    //         qIsCC = true;
    //     }
    //     else{
    //         qIsCC = false;
    //     }
    // }

    document.getElementById("q1img").src = lou[randCook][0];
    document.getElementById("q2img").src = lou[randNext][0];

    console.log(randCook,lou[randCook][0])
    console.log(randNext,lou[randNext][0])

    console.log(q1IsRight,qIsCC)

}

update()

function submitQuestions(){
   if(q1IsRight){
       if(qIsCC){
            if(document.getElementById("question1cc").checked){
                console.log("User is correct")
                setVal()
            }
       }
       else{
            if(document.getElementById("question1or").checked){
                console.log("User is correct")
                setVal()
            }
       }
   }
   else{
        if(qIsCC){
            if(document.getElementById("question2cc").checked){
                console.log("User is correct")
                setVal()
            }
        }
        else{
            if(document.getElementById("question2or").checked){
                console.log("User is correct")
                setVal()
            }
        }
   }
}

