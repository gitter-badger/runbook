######################################################################
# Cloud Routes Web Application
# -------------------------------------------------------------------
# CloudFlare IP Replacement - Forms Class
######################################################################

from wtforms import TextField, SelectField
from wtforms.validators import DataRequired, Email, IPAddress
from ..base import BaseReactForm


class ReactForm(BaseReactForm):

    ''' Class that creates a CloudFlair Reaction form for the dashboard '''
    email = TextField(
        "Email",
        validators=[Email(message='Email address invalid')])
    domain = TextField(
        "Domain",
        validators=[DataRequired(message='Domain is a required field')])
    apikey = TextField(
        "APIKey",
        validators=[DataRequired(message='API Key is a required field')])
    ip = TextField("IP",
        validators=[DataRequired(message='IP is a required field')])
    replaceip = TextField(
        "ReplaceIP", validators=[DataRequired(message='Replace IP is a required field')])
    failback = SelectField(
        "Failback",
        choices=[('manual', 'None'), ('automatic', 'Automatic')],
        validators=[DataRequired(message='Failback Method is a required field')])

if __name__ == '__main__':
    pass
