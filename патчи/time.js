
Things=[
"2018-01-02 23:21",
"2018-01-03 00:36",
"2018-01-03 13:45",
"2018-01-03 13:18",
"2018-01-03 14:12",
"2018-01-03 15:17",
"2018-01-03 15:26",
"2018-01-03 23:05",
"2018-01-04 13:31",
];
process.stdout.write("T=[");
for (var i = 0; i < Things.length; i++) {
	// console.log()
	a=Date.parse(Things[i]);
	process.stdout.write(String(a)+" ");
}
process.stdout.write("]\n");
