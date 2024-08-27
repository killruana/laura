# Camille - An AI assistant
# Copyright (C) 2024 Jonathan Tremesaygues <jonathan.tremesaygues@slaanesh.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
from django.contrib import admin

from camille.models import XMPPChannel, XMPPMessage


@admin.register(XMPPChannel)
class XMPPChannelAdmin(admin.ModelAdmin):
    list_display = ("jid", "llm_model", "prompt")


@admin.register(XMPPMessage)
class XMPPChannelAdmin(admin.ModelAdmin):
    list_display = ("channel", "timestamp", "sender", "is_agent", "body")
