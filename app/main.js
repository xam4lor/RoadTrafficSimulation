let canvas;
let context;
let lines = [
    /*{
		name: "Line UUID",
        start: { x: 0, y: 0 },
        end: { x: 100, y: 100 },
        color: [0, 0, 0, 1],
		connectStart: [],
		connectEnd: []
    }*/
];
let activeLine = null; // Currently active line when mouse is down
let hoveredLine = null; // Line under the mouse
let circleRadius = 15;
let backgroundColor = [230, 230, 230, 1];


/**
 * Call the callback with the RGBA values of the pixel under the mouse.
 * Baed on https://stackoverflow.com/a/8188781/102620130.
 * @param callback 
 */
function pixelOnMouseOver(callback) {
    let cv = context.canvas;

    cv.addEventListener(
        "mousemove",
        (e) => {
			let data = context.getImageData(0, 0, cv.width, cv.height).data;
            let idx = (e.offsetY * cv.width + e.offsetX) * 4;
            let parts = Array.prototype.slice.call(data, idx, idx + 4);
            callback.apply(context, parts);
        },
        false
    );
}

// Draw lines
window.addEventListener("load", function () {
    canvas = document.getElementById("canvas");
    context = canvas.getContext("2d");

	// Set canvas size
	canvas.width = window.innerWidth;
	canvas.height = window.innerHeight;

    pixelOnMouseOver(function (r, g, b, a) {
		// Find index based on color
		let index = 220 - r + b * 10;

		// If background color, do nothing
		if (r == backgroundColor[0] && g == backgroundColor[1] && b == backgroundColor[2] && a == backgroundColor[3])
			return;

		// If there is a activeLine, do nothing
		if (activeLine)
			return;

		// Else
		if (index == 255 || index >= lines.length)
			hoveredLine = null;
		else {
			// Set hovered line
			hoveredLine = lines[index];
		}
    });

    // Start the animation loop
    run();
});



// === Animation loop ===
function run() {
    context.clearRect(0, 0, canvas.width, canvas.height);

	// Draw background
	context.fillStyle = "rgba(" + backgroundColor.join(",") + ")";
	context.fillRect(0, 0, canvas.width, canvas.height);

    // Draw lines
    for (let i = 0; i < lines.length; ++i) {
        let line = lines[i];
        context.strokeStyle = "rgba(" + line.color.join(",") + ")";
        context.lineWidth = 20;

		// If hovered, thicker width
		if (hoveredLine == line) {
			context.lineWidth = 25;
		}

		// Line
        context.beginPath();
        context.moveTo(line.start.x, line.start.y);
        context.lineTo(line.end.x, line.end.y);
        context.stroke();
        context.closePath();

		// Draw a small black arrow at the middle of the line, indicating the direction
		context.fillStyle = "rgba(0, 0, 0, 1)";
		let middle = {
			x: (line.start.x + line.end.x) / 2,
			y: (line.start.y + line.end.y) / 2
		};
		let angle = Math.atan2(line.end.y - line.start.y, line.end.x - line.start.x);
		let arrowSize = 15;
		context.beginPath();
		context.moveTo(middle.x, middle.y);
		context.lineTo(middle.x - arrowSize * Math.cos(angle + Math.PI / 6), middle.y - arrowSize * Math.sin(angle + Math.PI / 6));
		context.lineTo(middle.x - arrowSize * Math.cos(angle - Math.PI / 6), middle.y - arrowSize * Math.sin(angle - Math.PI / 6));
		context.lineTo(middle.x, middle.y);
		context.fill();
		context.closePath();
		
		

		// Circle at start
		context.fillStyle = "rgba(0, 0, 0, 1)";
		context.beginPath();
		context.arc(line.start.x, line.start.y, circleRadius, 0, 2 * Math.PI);
		context.fill();
		context.closePath();

		// Circle at end
		context.beginPath();
		context.arc(line.end.x, line.end.y, circleRadius, 0, 2 * Math.PI);
		context.fill();
		context.closePath();
    }

    // Draw active line
    if (activeLine) {
        context.strokeStyle = "rgba(" + activeLine.color.join(",") + ")";
        context.lineWidth = 20;

        context.beginPath();
        context.moveTo(activeLine.start.x, activeLine.start.y);
        context.lineTo(mousePos.x, mousePos.y);
        context.stroke();
        context.closePath();
    }

    requestAnimationFrame(run);
}

function setLineConnections(newLine) {
	for (let i = 0; i < lines.length - 1; i++) {
		let line = lines[i];
		if (line == newLine)
			continue;

		let distStartStart = Math.sqrt(
			Math.pow(newLine.start.x - line.start.x, 2) +
			Math.pow(newLine.start.y - line.start.y, 2)
		);
		let distStartEnd = Math.sqrt(
			Math.pow(newLine.start.x - line.end.x, 2) +
			Math.pow(newLine.start.y - line.end.y, 2)
		);
		let distEndStart = Math.sqrt(
			Math.pow(newLine.end.x - line.start.x, 2) +
			Math.pow(newLine.end.y - line.start.y, 2)
		);
		let distEndEnd = Math.sqrt(
			Math.pow(newLine.end.x - line.end.x, 2) +
			Math.pow(newLine.end.y - line.end.y, 2)
		);

		// Set intersecting points, and push ids
		if (distStartStart < circleRadius) {
			newLine.start = line.start;
		}
		else if (distStartEnd < circleRadius) {
			newLine.start = line.end;
			newLine.connectStart.push(lines[i]);
			line.connectEnd.push(lines[lines.length - 1]);
		}
		else if (distEndStart < circleRadius) {
			newLine.end = line.start;
			newLine.connectEnd.push(lines[i]);
			line.connectStart.push(lines[lines.length - 1]);
		}
		else if (distEndEnd < circleRadius) {
			newLine.end = line.end;
		}
	}
}




// === Handle mouse events ===
let mouseDown = false;
let mouseDownTime = 0;
let UUIDIndex = 0;
window.addEventListener("load", function () {
createButtons();
context.canvas.addEventListener("mousedown", function (e) {
    if (mouseDown) return; // Prevent multiple calls (happens on Firefox)
    mouseDown = true;
	mouseDownTime = Date.now();

    // Add a new line as active line
    let currentLineCount = lines.length;
    activeLine = {
		name: "Line " + UUIDIndex++,
        start: { x: e.offsetX, y: e.offsetY },
        color: [
            220 - currentLineCount % 10,
            255 * 0.2,
            Math.floor(currentLineCount / 10),
            1
        ],
		connectStart: [],
		connectEnd: []
    };
});
window.addEventListener("mouseup", function (e) {
    mouseDown = false;
	// If mouse was down for less than 100ms, it's a click
	if (Date.now() - mouseDownTime < 100) {
		activeLine = null;
		return;
	}
    if (!activeLine) return;

	// If line is too short, remove it
	if (Math.sqrt(
		Math.pow(activeLine.start.x - e.offsetX, 2) +
		Math.pow(activeLine.start.y - e.offsetY, 2)
	) < 30) {
		activeLine = null;
		return;
	}

    // Add the active line to the list of lines
    activeLine.end = { x: e.offsetX, y: e.offsetY };
    lines.push(activeLine);
    activeLine = null;

	// Set new line's connections, if the two start and end circles are close enough
	setLineConnections(lines[lines.length - 1]);

	// If more than 100 lines, throw exception
	if (lines.length > 100)
		throw "Too many lines!";
});
window.addEventListener("mousemove", function (e) {
    mousePos = { x: e.offsetX, y: e.offsetY };
});
window.addEventListener("keydown", function (e) {
	// REMOVE HOVERED LINE
	if (e.key == "x" && hoveredLine) {
		// Remove connections
		for (let i = 0; i < hoveredLine.connectStart.length; ++i) {
			let line = hoveredLine.connectStart[i];
			let index = line.connectEnd.indexOf(hoveredLine);
			line.connectEnd.splice(index, 1);
		}
		for (let i = 0; i < hoveredLine.connectEnd.length; ++i) {
			let line = hoveredLine.connectEnd[i];
			let index = line.connectStart.indexOf(hoveredLine);
			line.connectStart.splice(index, 1);
		}

		// Remove hovered line
		let index = lines.indexOf(hoveredLine);
		lines.splice(index, 1);

		// Recompute colors
		for (let i = 0; i < lines.length; ++i) {
			let line = lines[i];
			line.color = [
				220 - i % 10,
				255 * 0.2,
				Math.floor(i / 10),
				1
			];
		}
	}

	// INVERT HOVERED LINE
	if (e.key == "i" && hoveredLine) {
		// Invert hovered line
		let temp = hoveredLine.start;
		hoveredLine.start = hoveredLine.end;
		hoveredLine.end = temp;

		// Clear every line's connections
		for (let i = 0; i < lines.length; i++) {
			lines[i].connectStart = [];
			lines[i].connectEnd = [];
		}

		// Recompute connections
		for (let i = 0; i < lines.length; i++)
			setLineConnections(lines[i]);
	}

    // ADD INPUT FLUX TO HOVERED LINE
    if (e.key == "a" && hoveredLine) {
        if (hoveredLine.color[1] == 127)
            hoveredLine.color[1] = 255 * 0.2;
        else
            hoveredLine.color[1] = 127;
    }
});
});




// === EXPORT DATA ===
function exportData() {
	let data = {
		"dimensions": {
			"x": canvas.width,
			"y": canvas.height
    	},
		"roads": []
	};
	for (let i = 0; i < lines.length; i++) {
		// Compute inRoads
		let inRoads = [];
		for (let j = 0; j < lines[i].connectStart.length; j++)
			inRoads.push(lines.indexOf(lines[i].connectStart[j]));

		// Compute outRoads
		let outRoads = [];
		for (let j = 0; j < lines[i].connectEnd.length; j++)
			outRoads.push(lines.indexOf(lines[i].connectEnd[j]));

        // Set inflow
        let inFlow = { type: "None" };
        if (lines[i].color[1] == 127) {
            let inFType = document.getElementById("road-type").value;
            if (inFType == "0") // a |sin(bt)|
                inFlow = {
                    "type": "sin",
                    "amplitude": parseFloat(document.getElementById("flux-a").value),
                    "frequency": parseFloat(document.getElementById("flux-b").value)
                };
            else if (inFType == "1") // a if t < b, else 0
                inFlow = {
                    "type": "if",
                    "rate": parseFloat(document.getElementById("flux-a").value),
                    "startTime": parseFloat(document.getElementById("flux-b").value)
                };
        }

		// Set road
		let line = lines[i];
		data.roads.push({
			"id": i,
			"name": "Road " + i,
			"start": {
				"x": line.start.x,
				"y": canvas.height - line.start.y
			},
			"end": {
				"x": line.end.x,
				"y": canvas.height - line.end.y
			},
			inRoads: inRoads,
			outRoads: outRoads,
			inFlow: inFlow
		});
	}
	
	// Download data
	let a = document.createElement("a");
	a.href = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data));
	a.download = "roads.json";
	a.click();
}


function createButtons() {
    // Create generate button
    document.getElementById("generate").addEventListener("click", function () {
        exportData();
    });

    // Create clear button
    document.getElementById("clear").addEventListener("click", function () {
        // Reload page
        location.reload();
    });
}
