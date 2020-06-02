from email_validator import validate_email, EmailNotValidError
def valid (email):
# email = "my+address@mydomain.tld"

 try:
  # Validate.
   valid = validate_email(email)

  # Update with the normalized form.
   email = valid.email
 except EmailNotValidError as e:
  # email is not valid, exception message is human-readable
   print(str(e))
   return False
#valid("sangitasapra@")
