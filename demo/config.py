#  Copyright 2020 Google LLC
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

hierarchy = {
    'service': 'Schema',
    'nested': [
        {
            'service': 'Google',
            'nested': [
                {
                    'service': 'GoogleProduct'
                },
                {
                    'service': 'GoogleArticle'
                },
                {
                    'service': 'GoogleEvent'
                },
                {
                    'service': 'GoogleRecipe'
                },
                {
                    'service': 'GoogleJobPosting'
                },
                {
                    'service': 'GoogleLocalBusiness'
                },
                {
                    'service': 'GoogleOrganization'
                },
                {
                    'service': 'GoogleVideo'
                },
                {
                    'service': 'GoogleMovie'
                },
                {
                    'service': 'GoogleCourse'
                },
                {
                    'service': 'GoogleSoftwareApplication'
                },
                {
                    'service': 'GoogleFAQ'
                },
                {
                    'service': 'GoogleQA'
                },
                {
                    'service': 'GoogleReview'
                }
            ]
        },
        {
            'service': 'Pinterest',
            'nested': [
                {
                    'service': 'PinterestProduct'
                },
                {
                    'service': 'PinterestArticle'
                },
                {
                    'service': 'PinterestRecipe'
                }
            ]
        },
        {
            'service': 'Bing',
            'nested': [
                {
                    'service': 'BingProduct'
                },
                {
                    'service': 'BingArticle'
                },
                {
                    'service': 'BingEvent'
                },
                {
                    'service': 'BingLocalBusiness'
                },
                {
                    'service': 'BingOrganization'
                }
            ]
        }
    ]
}
