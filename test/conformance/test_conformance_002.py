# SPDX-License-Identifier: Apache-2.0

# Copyright 2020 Contributors to OpenLEADR

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from openleadr import OpenADRClient, OpenADRServer, enums
from openleadr.utils import generate_id
from openleadr.messaging import create_message, parse_message
from datetime import datetime, timezone, timedelta

from pprint import pprint


@pytest.mark.asyncio
async def test_conformance_002():
    """
    The uid element is REQUIRED for each eiEventSignal interval. Within a sin-
    gle oadrDistributeEvent eiEventSignal, uid MUST be expressed as an inter-
    val number with a base of 0 and an increment of 1 for each subsequent in-
    terval.
    """
    event_id = generate_id()
    event = {'event_descriptor':
                {'event_id': event_id,
                 'modification_number': 0,
                 'modification_date': datetime.now(),
                 'priority': 0,
                 'market_context': 'MarketContext001',
                 'created_date_time': datetime.now(),
                 'event_status': enums.EVENT_STATUS.FAR,
                 'test_event': False,
                 'vtn_comment': 'No Comment'},
            'active_period':
                {'dtstart': datetime.now(),
                 'duration': timedelta(minutes=30)},
            'event_signals':
                [{'intervals': [{'duration': timedelta(minutes=10),
                                 'signal_payload': 1},
                                {'duration': timedelta(minutes=10),
                                 'signal_payload': 2},
                                {'duration': timedelta(minutes=10),
                                 'signal_payload': 3}],
                  'signal_name': enums.SIGNAL_NAME.SIMPLE,
                  'signal_type': enums.SIGNAL_TYPE.DELTA,
                  'signal_id': generate_id()
                }]
        }

    # Create a message with this event
    msg = create_message('oadrDistributeEvent',
                         response={'response_code': 200,
                                   'response_description': 'OK',
                                   'request_id': generate_id()},
                         request_id=generate_id(),
                         vtn_id=generate_id(),
                         events=[event])

    # Parse the message
    parsed_type, parsed_msg = parse_message(msg)
    assert parsed_type == 'oadrDistributeEvent'
    intervals = parsed_msg['events'][0]['event_signals'][0]['intervals']

    # Verify that the interval uid's are numbered consecutively and starting at 0
    assert intervals[0]['uid'] == 0
    assert intervals[0]['signal_payload'] == 1
    assert intervals[1]['uid'] == 1
    assert intervals[1]['signal_payload'] == 2
    assert intervals[2]['uid'] == 2
    assert intervals[2]['signal_payload'] == 3
