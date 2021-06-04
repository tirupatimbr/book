from rest_framework.schemas import AutoSchema,ManualSchema
import coreapi,coreschema


register_schema = AutoSchema(manual_fields=[coreapi.Field("username",required=True,type="string",description="enter username"),
                    coreapi.Field("password1",required=True,type="string",description="enter password"),
                    coreapi.Field("password2",required=True,type="string",description="confirm password"),
                    coreapi.Field("email",required=True,type="string",description="enter email")])

mobile_schema = AutoSchema(manual_fields=[coreapi.Field("brand",required=True,type="string",description="enter brand name"),
                    coreapi.Field("mobile_model",required=True,type="string",description="enter mobile model"),
                    coreapi.Field("price",required=True,type="integer",description="enter mobile price"),
                    coreapi.Field("stock",required=True,type="integer",description="enter available stock position"),])

mobile_get_schema = AutoSchema(manual_fields=[coreapi.Field('id',type="integer",description="enter id number to get details",required=True)])

mobile_delete_schema = AutoSchema(manual_fields=[coreapi.Field("id",type="integer",description="enter id number to delete details",required=True)])

author_chema =AutoSchema(manual_fields=[coreapi.Field("name",required=True,type="string",description="enter author name"),
                    coreapi.Field("age",required=True,type="string",description="enter author age"),
                    coreapi.Field("place",required=True,type="string",description="enter author place")])

login_schema =AutoSchema(manual_fields=[coreapi.Field("username",required=True,type="string",description="enter your username"),
                    coreapi.Field("password",required=True,type="string",description="enter your password"),])

reset_password_schema = AutoSchema(manual_fields=[coreapi.Field("username",required=True,type="string",description="enter username"),
                    coreapi.Field("password",required=True,type="string",description="enter password"),
                    coreapi.Field("email",required=True,type="string",description="enter email address to sent OTP"),])