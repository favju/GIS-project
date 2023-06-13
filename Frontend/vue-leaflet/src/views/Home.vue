<template>
    <h1>Explore the resort</h1>
    <div class="mapAndInfo">
        <Map ref="mapy" />
        <div>
            One day we will be able to display something on the map and at this moment you will be able to click on it and
            learn many beautiful thing about it
        </div>
    </div>

    <button @click="testAddLayer()">hello</button>
</template>
<script>
import Map from '../components/Map.vue'
export default {
    name: "Home",
    components: {
        Map
    },
    data() {
        return {
            skilift: {
                "type": "FeatureCollection",
                "name": "skilift",
                "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:EPSG::21781" } },
                "features": [
                    { "type": "Feature", "properties": { "id": 1, "name": "Grand Chamossaire", "length": 1098.546599, "maxSeat": 8, "type": "Télésiège" }, "geometry": { "type": "MultiLineString", "coordinates": [[[570977.149093960644677, 130646.476673743658466, 0.0], [571850.833295980701223, 129980.533324277654174, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 2, "name": "Lac de Bretaye", "length": 240.959584, "maxSeat": 1, "type": "Télésiège" }, "geometry": { "type": "MultiLineString", "coordinates": [[[571887.725526406429708, 130193.134576806958648, 0.0], [571831.043873553164303, 130427.332594496736419, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 3, "name": "Lac Noir-Bretaye", "length": 570.108049, "maxSeat": 1, "type": "Assiette" }, "geometry": { "type": "MultiLineString", "coordinates": [[[572262.2476248415187, 130685.488157092957408, 0.0], [572035.559127291897312, 130463.069940739049343, 0.0], [571995.02601531392429, 130393.157229897988145, 0.0], [571992.50807704043109, 130221.46127335523488, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 4, "name": "Lac Noir-Chaux Ronde", "length": 916.143726, "maxSeat": 8, "type": "Assiette" }, "geometry": { "type": "MultiLineString", "coordinates": [[[572246.995935100014322, 130744.794956343583181, 0.0], [572766.366922184592113, 129990.094283685932169, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 5, "name": "Chaux Ronde 1", "length": 768.771469, "maxSeat": 2, "type": "Arbalète" }, "geometry": { "type": "MultiLineString", "coordinates": [[[571899.324985294369981, 130033.459949870812125, 0.0], [572666.244925458566286, 129980.13662365890923, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 6, "name": "Chaux Ronde 2", "length": 768.537512, "maxSeat": 1, "type": "Assiette" }, "geometry": { "type": "MultiLineString", "coordinates": [[[571898.399476529913954, 130025.245035794156138, 0.0], [572665.127534509636462, 129972.538365205764421, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 7, "name": "Rasse-Chaux Ronde", "length": 2131.648343, "maxSeat": 8, "type": "Télésiège" }, "geometry": { "type": "MultiLineString", "coordinates": [[[572683.484588858205825, 129971.951603617606452, 0.0], [573096.142239683773369, 127880.627065567794489, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 8, "name": "Petit Chamossaire", "length": 993.994519, "maxSeat": 8, "type": "Télésiège" }, "geometry": { "type": "MultiLineString", "coordinates": [[[571391.803069215733558, 131191.560495301004266, 0.0], [572368.136220525950193, 131005.016449011658551, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 9, "name": "Combe d'Orsay", "length": 657.921091, "maxSeat": 1, "type": "Assiete" }, "geometry": { "type": "MultiLineString", "coordinates": [[[571186.319303796277381, 130227.27153189019009, 0.0], [571097.621608589426614, 130132.507322962410399, 0.0], [571060.709293537656777, 130122.445603072206723, 0.0], [570696.464297024300322, 130234.626031411637086, 0.0], [570618.215409452444874, 130310.127879567400669, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 10, "name": "Bretaye-Orsay", "length": 697.519059, "maxSeat": 1, "type": "Assiete" }, "geometry": { "type": "MultiLineString", "coordinates": [[[571158.108694368624128, 130097.720710470617632, 0.0], [571331.736536144744605, 130032.249486405969947, 0.0], [571647.699821620364673, 130030.543111785096698, 0.0], [571764.124689477146603, 130063.01245045394171, 0.0], [571839.212148923543282, 130060.740146175172413, 0.0]]] } },
                    { "type": "Feature", "properties": { "id": 11, "name": "Roc D'Orsay", "length": 2160.619156, "maxSeat": 8, "type": "Cabine" }, "geometry": { "type": "MultiLineString", "coordinates": [[[570439.666255393764004, 128098.261780374319642, 0.0], [571134.101429424597882, 130144.24196722630586, 0.0]]] } }
                ]
            }
        }
    },
    mounted() {
        //L.geoJSON(this.skilift.features).addTo(this.$refs.mapy.mapDiv);
    },
    methods: {
        testAddLayer() {
            console.log("coucou")
            //L.geoJSON(this.skilift.features).addTo(this.$refs.mapy.mapDiv);
            var myLines = {
                "type": "FeatureCollection",
                "features": [
                    {
                        "id": 1,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.061777820889852,
                                        46.32658352549184,
                                        0.0
                                    ],
                                    [
                                        7.07316297104453,
                                        46.320630320259575,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Grand Chamossaire",
                            "length": "1098.5466",
                            "maxseat": 8,
                            "type": "Télésiège"
                        }
                    },
                    {
                        "id": 2,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.073629077305652,
                                        46.32254433015707,
                                        0.0
                                    ],
                                    [
                                        7.072878901280944,
                                        46.324648681813,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Lac de Bretaye",
                            "length": "240.9596",
                            "maxseat": 1,
                            "type": "Télésiège"
                        }
                    },
                    {
                        "id": 3,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.078462417674921,
                                        46.326988931944015,
                                        0.0
                                    ],
                                    [
                                        7.075532270198576,
                                        46.324978731942906,
                                        0.0
                                    ],
                                    [
                                        7.07501018711162,
                                        46.32434813600384,
                                        0.0
                                    ],
                                    [
                                        7.074987860783339,
                                        46.322803535250245,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Lac Noir-Bretaye",
                            "length": "570.1080",
                            "maxseat": 1,
                            "type": "Assiette"
                        }
                    },
                    {
                        "id": 4,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.078260824718225,
                                        46.327521795800976,
                                        0.0
                                    ],
                                    [
                                        7.085049262393745,
                                        46.32075419337714,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Lac Noir-Chaux Ronde",
                            "length": "916.1437",
                            "maxseat": 8,
                            "type": "Assiette"
                        }
                    },
                    {
                        "id": 5,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.073789357452663,
                                        46.32110846000984,
                                        0.0
                                    ],
                                    [
                                        7.083749909988617,
                                        46.320660538625205,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Chaux Ronde 1",
                            "length": "768.7715",
                            "maxseat": 2,
                            "type": "Arbalète"
                        }
                    },
                    {
                        "id": 6,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.073777838651711,
                                        46.321034523700675,
                                        0.0
                                    ],
                                    [
                                        7.083735850080176,
                                        46.32059214264119,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Chaux Ronde 2",
                            "length": "768.5375",
                            "maxseat": 1,
                            "type": "Assiette"
                        }
                    },
                    {
                        "id": 7,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.083974223705043,
                                        46.32058761367021,
                                        0.0
                                    ],
                                    [
                                        7.089453234285955,
                                        46.30179174858916,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Rasse-Chaux Ronde",
                            "length": "2131.6483",
                            "maxseat": 8,
                            "type": "Télésiège"
                        }
                    },
                    {
                        "id": 8,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.06712845016349,
                                        46.331504685993345,
                                        0.0
                                    ],
                                    [
                                        7.079818345804262,
                                        46.32986763708535,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Petit Chamossaire",
                            "length": "993.9945",
                            "maxseat": 8,
                            "type": "Télésiège"
                        }
                    },
                    {
                        "id": 9,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.064519922599697,
                                        46.322821591821686,
                                        0.0
                                    ],
                                    [
                                        7.063374173279666,
                                        46.3219653156166,
                                        0.0
                                    ],
                                    [
                                        7.062895537891435,
                                        46.321873210853305,
                                        0.0
                                    ],
                                    [
                                        7.058159167459981,
                                        46.322866489955366,
                                        0.0
                                    ],
                                    [
                                        7.057138398890318,
                                        46.32354223898237,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Combe d'Orsay",
                            "length": "657.9211",
                            "maxseat": 1,
                            "type": "Assiete"
                        }
                    },
                    {
                        "id": 10,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.064161689949776,
                                        46.32165500021003,
                                        0.0
                                    ],
                                    [
                                        7.066420077313878,
                                        46.32107350910214,
                                        0.0
                                    ],
                                    [
                                        7.070522528441462,
                                        46.32107161343148,
                                        0.0
                                    ],
                                    [
                                        7.072032168231004,
                                        46.32136861214563,
                                        0.0
                                    ],
                                    [
                                        7.073007218563503,
                                        46.32135133400353,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Bretaye-Orsay",
                            "length": "697.5191",
                            "maxseat": 1,
                            "type": "Assiete"
                        }
                    },
                    {
                        "id": 11,
                        "type": "Feature",
                        "geometry": {
                            "type": "MultiLineString",
                            "coordinates": [
                                [
                                    [
                                        7.054960976333546,
                                        46.30363750906064,
                                        0.0
                                    ],
                                    [
                                        7.063847090752126,
                                        46.32207244853415,
                                        0.0
                                    ]
                                ]
                            ]
                        },
                        "properties": {
                            "name": "Roc D'Orsay",
                            "length": "2160.6192",
                            "maxseat": 8,
                            "type": "Cabine"
                        }
                    }
                ]
            };


            var myStyle = {
                "color": "blue",
                "weight": 5,
                "opacity": 0.65
            };

            L.geoJSON(myLines, {
                style: myStyle
            }).addTo(this.$refs.mapy.mapDiv);
        }
    }
}

</script>

<style>
.mapAndInfo {
    display: flex;
}
</style>