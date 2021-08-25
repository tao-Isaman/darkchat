<html>
    <head>
        <title>Chat</title>
<link rel="stylesheet" href="https://unpkg.com/terminal.css@0.7.2/dist/terminal.min.css" />
<link rel="stylesheet" href="https://unpkg.com/terminal.css@0.7.1/dist/terminal.min.css" />
<link rel="stylesheet" href="https://unpkg.com/terminal.css@0.7.1/dist/terminal.min.css" />
    </head>
<style>
      :root {
        --global-font-size: 15px;
        --global-line-height: 1.4em;
        --global-space: 10px;
        --font-stack: Menlo, Monaco, Lucida Console, Liberation Mono,
          DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace,
          serif;
        --mono-font-stack: Menlo, Monaco, Lucida Console, Liberation Mono,
          DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace,
          serif;
        --background-color: #222225;
        --page-width: 60em;
        --font-color: #e8e9ed;
        --invert-font-color: #222225;
        --secondary-color: #a3abba;
        --tertiary-color: #a3abba;
        --primary-color: #62c4ff;
        --error-color: #ff3c74;
        --progress-bar-background: #3f3f44;
        --progress-bar-fill: #62c4ff;
        --code-bg-color: #3f3f44;
        --input-style: solid;
        --display-h1-decoration: none;
      }
    </style>
    <body class="terminal">
        <div class="container">
        <h1>Darkchat</h1>
        <h2>Your ID: <span id="ws-id">12345</span></h2>
        <p id='y_messages'> Your : hello world </p>
        <p id='y_messages'> User # 12345 : Hi </p>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
        </form>
        </p>
        </div>
    </body>
</html>