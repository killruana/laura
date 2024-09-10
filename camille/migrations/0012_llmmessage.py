# Generated by Django 5.1.1 on 2024-09-05 21:52

import django.db.models.deletion
from django.db import migrations, models


def migrate_messages(apps, schema_editor):
    XMPPMessage = apps.get_model("camille", "XMPPMessage")
    LLMMessage = apps.get_model("camille", "LLMMessage")

    for xmpp_message in XMPPMessage.objects.all():
        LLMMessage.objects.create(
            conversation=xmpp_message.channel.conversation,
            timestamp=xmpp_message.timestamp,
            is_agent=xmpp_message.is_agent,
            sender=xmpp_message.sender,
            content=xmpp_message.body,
        )


def migrate_messages_reverse(apps, schema_editor):
    XMPPMessage = apps.get_model("camille", "XMPPMessage")
    LLMMessage = apps.get_model("camille", "LLMMessage")

    for llm_message in LLMMessage.objects.filter(
        conversation__xmpp_channel__isnull=False
    ):
        XMPPMessage.objects.create(
            channel=llm_message.conversation.xmppchannel,
            timestamp=llm_message.timestamp,
            is_agent=llm_message.is_agent,
            sender=llm_message.sender,
            body=llm_message.content,
        )


class Migration(migrations.Migration):

    dependencies = [
        (
            "camille",
            "0009_llmconversation_xmppchannel_conversation_squashed_0011_remove_xmppchannel_llm_model_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="LLMMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("is_agent", models.BooleanField(default=False)),
                ("sender", models.CharField(max_length=255)),
                ("content", models.TextField()),
                (
                    "conversation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="messages",
                        to="camille.llmconversation",
                    ),
                ),
            ],
        ),
        migrations.RunPython(
            migrate_messages, reverse_code=migrate_messages_reverse, atomic=True
        ),
        migrations.AlterField(
            model_name="xmppchannel",
            name="conversation",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="xmpp_channel",
                related_query_name="xmpp_channel",
                to="camille.llmconversation",
            ),
        ),
        migrations.DeleteModel(
            name="XMPPMessage",
        ),
    ]
