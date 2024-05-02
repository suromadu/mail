
from .models import UserFidoKeys

from fido2.webauthn import PublicKeyCredentialRpEntity, PublicKeyCredentialUserEntity, AttestedCredentialData, UserVerificationRequirement
from fido2.server import Fido2Server
from fido2.utils import websafe_decode, websafe_encode
import fido2.features


def set_json_mapping():
    try:
        fido2.features.webauthn_json_mapping.enabled = True
    except ValueError:
        pass


def create_fido2_server():
    rp = PublicKeyCredentialRpEntity(name="Demo server", id="localhost")
    return Fido2Server(rp)


def get_creds_from_user(user_id):
    return [AttestedCredentialData(websafe_decode(uf.credential_data)) for uf in UserFidoKeys.objects.filter(user=user_id)]


def begin_registration(request):
    set_json_mapping()
    server = create_fido2_server()
    options, state = server.register_begin(
        PublicKeyCredentialUserEntity(
            id=request.user.pk,
            name=request.user.username.encode('utf-8'),
            display_name=request.user.username,
        ),
        get_creds_from_user(request.user.pk),
        user_verification=UserVerificationRequirement.DISCOURAGED,
        extensions={"credentialProtectionPolicy":"userVerificationOptional"}
    )
    request.session['fido2_state'] = state
    return options


def end_registration(data, fido2_state, user_id):
    set_json_mapping()
    server = create_fido2_server()
    auth_data = server.register_complete(
        fido2_state,
        data
        )
    return websafe_encode(auth_data.credential_data)