use futeba;
db.users.find({
	loc:{
		$near: {
			$geometry: {
				type:'Point',
				coordinates: [-23.5621126, -46.5682175]},
			$maxDistance:4000
		}
	}
})
