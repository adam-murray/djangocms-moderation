from django.core.exceptions import ImproperlyConfigured
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.html import format_html

from cms.app_base import CMSAppConfig, CMSAppExtension
from cms.models import PageContent


def get_copy_content_expiry_button(obj):
    """
    Return a user friendly link to copy a content expiry to other Moderation Request Items
    link redirects to view which handles this
    """
    version = obj.moderation_request.version

    if hasattr(version, "contentexpiry"):
        content_expiry = version.contentexpiry
        view_endpoint = format_html(
            "{}?collection__id={}&?moderation_request__id={}&_popup=1",
            reverse("admin:djangocms_moderation_moderationrequesttreenode_copy", ),
            obj.pk,
            obj.moderation_request.pk,
        )
        return render_to_string(
            "admin/djangocms_moderation/icons/calendar_copy_icon.html", {
                "url": view_endpoint,
                "content_expiry_id": f"content_expiry_{content_expiry.pk}",
                "moderation_request_id": f"moderation_request_{obj.moderation_request.pk}"
            }
        )
    return ""


class ModerationExtension(CMSAppExtension):
    def __init__(self):
        self.moderated_models = []
        self.moderation_request_changelist_actions = [get_copy_content_expiry_button, ]
        self.moderation_request_changelist_fields = []

    def handle_moderation_request_changelist_actions(self, moderation_request_changelist_actions):
        self.moderation_request_changelist_actions.extend(moderation_request_changelist_actions)

    def handle_moderation_request_changelist_fields(self, moderation_request_changelist_fields):
        self.moderation_request_changelist_fields.extend(moderation_request_changelist_fields)

    def configure_app(self, cms_config):
        versioning_enabled = getattr(cms_config, "djangocms_versioning_enabled", False)
        moderated_models = getattr(cms_config, "moderated_models", [])

        if not versioning_enabled:
            raise ImproperlyConfigured("Versioning needs to be enabled for Moderation")

        self.moderated_models.extend(moderated_models)

        if hasattr(cms_config, "moderation_request_changelist_actions"):
            self.handle_moderation_request_changelist_actions(cms_config.moderation_request_changelist_actions)

        if hasattr(cms_config, "moderation_request_changelist_fields"):
            self.handle_moderation_request_changelist_fields(cms_config.moderation_request_changelist_fields)


class CoreCMSAppConfig(CMSAppConfig):
    djangocms_moderation_enabled = True
    djangocms_versioning_enabled = True
    moderated_models = [PageContent]
    versioning = []

