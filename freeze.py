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

"""
Freeze the Flask app to static files for GitHub Pages deployment.
"""

import os
import sys
import json
import shutil
from pathlib import Path

# Add demo directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'demo'))

from app import app
import config

def freeze():
    """Generate static files from Flask app."""

    output_dir = Path('demo')

    # Create demo/index.html from the Flask route
    with app.test_client() as client:
        # Get the main page
        response = client.get('/')
        index_html = response.data.decode('utf-8')

        # Replace Flask template tags with actual paths
        index_html = index_html.replace(
            "{{ url_for('static', filename='css/scc.css') }}",
            "static/css/scc.css"
        )
        index_html = index_html.replace(
            "{{ url_for('static', filename='js/libs/schemarama.bundle.js') }}",
            "static/js/libs/schemarama.bundle.js"
        )
        index_html = index_html.replace(
            "{{ url_for('static', filename='js/scc/shex.js') }}",
            "static/js/scc/shex.js"
        )
        index_html = index_html.replace(
            "{{ url_for('static', filename='js/scc/shacl.js') }}",
            "static/js/scc/shacl.js"
        )
        index_html = index_html.replace(
            "{{ url_for('static', filename='js/scc/layout.js') }}",
            "static/js/scc/layout.js"
        )
        index_html = index_html.replace(
            "{{ url_for('static', filename='js/scc/core.js') }}",
            "static/js/scc/core.js"
        )
        index_html = index_html.replace(
            "{{ url_for('static', filename='images/icons/play_arrow.svg') }}",
            "static/images/icons/play_arrow.svg"
        )

        with open(output_dir / 'index.html', 'w') as f:
            f.write(index_html)

        print(f"✓ Created demo/index.html")

        # Create hierarchy.json
        hierarchy_response = client.get('/hierarchy')
        with open(output_dir / 'hierarchy.json', 'w') as f:
            json.dump(json.loads(hierarchy_response.data), f, indent=2)

        print(f"✓ Created demo/hierarchy.json")

        # Copy shapeToService.json to demo/services-map.json
        shutil.copy(
            'demo/validation/shapeToService.json',
            'demo/services-map.json'
        )
        print(f"✓ Created demo/services-map.json")

        # Copy full.shexj to demo/shex-shapes.json
        shutil.copy(
            'demo/validation/shex/full.shexj',
            'demo/shex-shapes.json'
        )
        print(f"✓ Created demo/shex-shapes.json")

        # Copy full.shacl to demo/shacl-shapes.ttl
        if os.path.exists('demo/validation/shacl/full.shacl'):
            shutil.copy(
                'demo/validation/shacl/full.shacl',
                'demo/shacl-shapes.ttl'
            )
            print(f"✓ Created demo/shacl-shapes.ttl")

        # Copy subclasses.ttl
        if os.path.exists('demo/validation/shacl/subclasses.ttl'):
            shutil.copy(
                'demo/validation/shacl/subclasses.ttl',
                'demo/shacl-subclasses.ttl'
            )
            print(f"✓ Created demo/shacl-subclasses.ttl")

if __name__ == '__main__':
    freeze()
    print("\n✅ Static site generated successfully!")
    print("📁 Output: demo/")
