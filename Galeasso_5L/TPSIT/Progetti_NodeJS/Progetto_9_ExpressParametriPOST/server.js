app.use(express.json());
app.use(
	express.urlencode({
		extended: true,
	})
);

app.use(cors());
app.option("*", cors());
