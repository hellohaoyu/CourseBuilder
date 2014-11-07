# Copyright 2014. Haoyu Chen All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""FAQ module."""

__author__ = 'Haoyu Chen (hc6as@virginia.edu)'

from tools import verify
from models import content

from controllers import utils_faq
from models import custom_modules
from controllers import utils_allresources

custom_module = None

def notify():
    print "It has been notify_module_enabled"
    
def register_module():
    """Registers this module in the registry."""

    # provide parser to verify
    verify.parse_content = content.parse_string_in_scope

    # setup routes
    courses_routes = [('/faq', utils_faq.FaqHandler),('/allresources', utils_allresources.AllResourcesHandler)]

    global custom_module
    custom_module = custom_modules.Module(
        'Course',
        'FAQ Module',
        [], courses_routes, notify_module_enabled = notify)

    return custom_module