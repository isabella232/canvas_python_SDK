###Python SDK for Canvas Apps

#### Installing

To get started you'll need to install the optimizely_canvas_sdk package:

```
pip install optimizely_canvas_sdk
```

#### Usage

Note: This example request is properly signed (albeit with a weak demo secret), so feel free to try actually parsing it with this package.

Say you host your Canvas app at https://michelangelo.appspot.com/canvas. If Optimizely serves a Canvas request like this:

```
https://michelangelo.appspot.com/canvas?signed_request=ZDhiNWFkMTA0ZjFjZjFhMDU0NWQzZjE5MTI1YWZlNTk0YjQzYTU5Y2NiMjgxZjY2NTgxYmM3YzYyYjgxNzAwMg%3D%3D.eyJjb250ZXh0Ijp7ImVudmlyb25tZW50Ijp7ImN1cnJlbnRfcHJvamVjdCI6MTIzNDU2NywiY3VycmVudF9hY2NvdW50Ijo3NjU0MzIxfSwiY2xpZW50Ijp7ImFjY2Vzc190b2tlbiI6IjEyMzQ1Njc4OTBhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejEyMyIsInRva2VuX3R5cGUiOiJiZWFyZXIiLCJleHBpcmVzX2luIjo3MjAwfSwidXNlciI6eyJlbWFpbCI6ImpvbkBvcHRpbWl6ZWx5LmNvbSJ9fX0%3D
```
You can extract the URL-decoded value of the signed_request parameter, grab your Canvas app's OAuth client secret from [this page](https://app.optimizely.com/accountsettings/apps/developers), and invoke the SDK package's extract_user_context function with client secret and the signed request value:

```
import optimizely_canvas_sdk

var signed_request = 'ZDhiNWFkMTA0ZjFjZjFhMDU0NWQzZjE5MTI1YWZlNTk0YjQzYTU5Y2NiMjgxZjY2NTgxYmM3YzYyYjgxNzAwMg==.eyJjb250ZXh0Ijp7ImVudmlyb25tZW50Ijp7ImN1cnJlbnRfcHJvamVjdCI6MTIzNDU2NywiY3VycmVudF9hY2NvdW50Ijo3NjU0MzIxfSwiY2xpZW50Ijp7ImFjY2Vzc190b2tlbiI6IjEyMzQ1Njc4OTBhYmNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ejEyMyIsInRva2VuX3R5cGUiOiJiZWFyZXIiLCJleHBpcmVzX2luIjo3MjAwfSwidXNlciI6eyJlbWFpbCI6ImpvbkBvcHRpbWl6ZWx5LmNvbSJ9fX0=';
 
canvas_app_values = optimizely_canvas_sdk.extract_user_context(signed_request, 'my_oauth_client_secret') 
``` 

canvas_app_values will then be a nested dictionary like this:
```
{ context:
   { environment: { current_project: 1234567, current_account: 7654321 },
     client:
      { access_token: '1234567890abcdefghijklmnopqrstuvwxyz123',
        token_type: 'bearer',
        expires_in: 7200 },
     user: { email: 'rebecca@optimizely.com' }
   }
}
```

#### Error Handling

In the event the request is not properly signed, an error will be thrown:
```
OptimizelyCanvasValidationError: Request not properly signed.
```

If an error is thrown, you should immediately return an HTTP 401 to the user and assume the request was malicious. Do not do any processing for the user or expose any data to the user.