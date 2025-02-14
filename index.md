<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wildfire Hazard Analysis</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/showdown/2.0.3/showdown.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f9fa;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .container {
            max-width: 800px;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            text-align: center;
        }
        h1 {
            color: #333;
        }
        .link-container {
            margin-top: 20px;
        }
        a {
            display: block;
            font-size: 18px;
            margin: 10px 0;
            text-decoration: none;
            color: blue;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
        #content {
            text-align: left;
            margin-top: 30px;
            padding: 20px;
            border-radius: 5px;
            background: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Wildfire Hazard Analysis</h1>
        <p>A critical evaluation of Oregon State's wildfire hazard model.</p>

        <div class="link-container">
            <a href="#" onclick="loadMarkdown('abstract.md')">📄 Read Abstract</a>
            <a href="#" onclick="loadMarkdown('wildfiremodelanalysis.html')">📄 Read Full Paper</a>
            <a href="https://github.com/DataZenith/wildfireHazardAnalysis" target="_blank">🔗 View on GitHub</a>
        </div>

        <div id="content">
            <p>Select a document above to view it.</p>
        </div>
    </div>

    <script>
        function loadMarkdown(file) {
            // Get the raw GitHub link for the Markdown file
            const rawGitHubUrl = `https://raw.githubusercontent.com/DataZenith/wildfireHazardAnalysis/main/${file}`;

            fetch(rawGitHubUrl)
                .then(response => response.text())
                .then(md => {
                    let converter = new showdown.Converter();
                    document.getElementById("content").innerHTML = converter.makeHtml(md);
                })
                .catch(error => console.error('Error loading Markdown:', error));
        }
    </script>

</body>
</html>
