###Python SDK for Canvas Apps

#### Authentication

To get started you'll need to import the package:
```
import canvas_SDK

```

Add the signed request and your Oauth Client secret:

```
canvas_app_values = canvas_SDK.CanvasValidation(signed_request, optimizely_oauth_client_secret) 

``` 

Extract the user context Object:

```
user_context = canvas_app_values.extractUserContext()

```

