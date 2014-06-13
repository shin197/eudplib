"""
Useful enumeration.
"""

DefUnitID = {
	"Terran Marine" : 0,
	"Terran Ghost" : 1,
	"Terran Vulture" : 2,
	"Terran Goliath" : 3,
	"Goliath Turret" : 4,
	"Terran Siege Tank (Tank Mode)" : 5,
	"Siege Tank Turret (Tank Mode)" : 6,
	"Terran SCV" : 7,
	"Terran Wraith" : 8,
	"Terran Science Vessel" : 9,
	"Gui Montag (Firebat)" : 10,
	"Terran Dropship" : 11,
	"Terran Battlecruiser" : 12,
	"Spider Mine" : 13,
	"Nuclear Missile" : 14,
	"Terran Civilian" : 15,
	"Sarah Kerrigan (Ghost)" : 16,
	"Alan Schezar (Goliath)" : 17,
	"Alan Schezar Turret" : 18,
	"Jim Raynor (Vulture)" : 19,
	"Jim Raynor (Marine)" : 20,
	"Tom Kazansky (Wraith)" : 21,
	"Magellan (Science Vessel)" : 22,
	"Edmund Duke (Tank Mode)" : 23,
	"Edmund Duke Turret (Tank Mode)" : 24,
	"Edmund Duke (Siege Mode)" : 25,
	"Edmund Duke Turret (Siege Mode)" : 26,
	"Arcturus Mengsk (Battlecruiser)" : 27,
	"Hyperion (Battlecruiser)" : 28,
	"Norad II (Battlecruiser)" : 29,
	"Terran Siege Tank (Siege Mode)" : 30,
	"Siege Tank Turret (Siege Mode)" : 31,
	"Terran Firebat" : 32,
	"Scanner Sweep" : 33,
	"Terran Medic" : 34,
	"Zerg Larva" : 35,
	"Zerg Egg" : 36,
	"Zerg Zergling" : 37,
	"Zerg Hydralisk" : 38,
	"Zerg Ultralisk" : 39,
	"Zerg Broodling" : 40,
	"Zerg Drone" : 41,
	"Zerg Overlord" : 42,
	"Zerg Mutalisk" : 43,
	"Zerg Guardian" : 44,
	"Zerg Queen" : 45,
	"Zerg Defiler" : 46,
	"Zerg Scourge" : 47,
	"Torrasque (Ultralisk)" : 48,
	"Matriarch (Queen)" : 49,
	"Infested Terran" : 50,
	"Infested Kerrigan (Infested Terran)" : 51,
	"Unclean One (Defiler)" : 52,
	"Hunter Killer (Hydralisk)" : 53,
	"Devouring One (Zergling)" : 54,
	"Kukulza (Mutalisk)" : 55,
	"Kukulza (Guardian)" : 56,
	"Yggdrasill (Overlord)" : 57,
	"Terran Valkyrie" : 58,
	"Mutalisk Cocoon" : 59,
	"Protoss Corsair" : 60,
	"Protoss Dark Templar (Unit)" : 61,
	"Zerg Devourer" : 62,
	"Protoss Dark Archon" : 63,
	"Protoss Probe" : 64,
	"Protoss Zealot" : 65,
	"Protoss Dragoon" : 66,
	"Protoss High Templar" : 67,
	"Protoss Archon" : 68,
	"Protoss Shuttle" : 69,
	"Protoss Scout" : 70,
	"Protoss Arbiter" : 71,
	"Protoss Carrier" : 72,
	"Protoss Interceptor" : 73,
	"Protoss Dark Templar (Hero)" : 74,
	"Zeratul (Dark Templar)" : 75,
	"Tassadar/Zeratul (Archon)" : 76,
	"Fenix (Zealot)" : 77,
	"Fenix (Dragoon)" : 78,
	"Tassadar (Templar)" : 79,
	"Mojo (Scout)" : 80,
	"Warbringer (Reaver)" : 81,
	"Gantrithor (Carrier)" : 82,
	"Protoss Reaver" : 83,
	"Protoss Observer" : 84,
	"Protoss Scarab" : 85,
	"Danimoth (Arbiter)" : 86,
	"Aldaris (Templar)" : 87,
	"Artanis (Scout)" : 88,
	"Rhynadon (Badlands Critter)" : 89,
	"Bengalaas (Jungle Critter)" : 90,
	"Cargo Ship (Unused)" : 91,
	"Mercenary Gunship (Unused)" : 92,
	"Scantid (Desert Critter)" : 93,
	"Kakaru (Twilight Critter)" : 94,
	"Ragnasaur (Ashworld Critter)" : 95,
	"Ursadon (Ice World Critter)" : 96,
	"Lurker Egg" : 97,
	"Raszagal (Corsair)" : 98,
	"Samir Duran (Ghost)" : 99,
	"Alexei Stukov (Ghost)" : 100,
	"Map Revealer" : 101,
	"Gerard DuGalle (BattleCruiser)" : 102,
	"Zerg Lurker" : 103,
	"Infested Duran (Infested Terran)" : 104,
	"Disruption Web" : 105,
	"Terran Command Center" : 106,
	"Terran Comsat Station" : 107,
	"Terran Nuclear Silo" : 108,
	"Terran Supply Depot" : 109,
	"Terran Refinery" : 110,
	"Terran Barracks" : 111,
	"Terran Academy" : 112,
	"Terran Factory" : 113,
	"Terran Starport" : 114,
	"Terran Control Tower" : 115,
	"Terran Science Facility" : 116,
	"Terran Covert Ops" : 117,
	"Terran Physics Lab" : 118,
	"Starbase (Unused)" : 119,
	"Terran Machine Shop" : 120,
	"Repair Bay (Unused)" : 121,
	"Terran Engineering Bay" : 122,
	"Terran Armory" : 123,
	"Terran Missile Turret" : 124,
	"Terran Bunker" : 125,
	"Norad II (Crashed)" : 126,
	"Ion Cannon" : 127,
	"Uraj Crystal" : 128,
	"Khalis Crystal" : 129,
	"Infested Command Center" : 130,
	"Zerg Hatchery" : 131,
	"Zerg Lair" : 132,
	"Zerg Hive" : 133,
	"Zerg Nydus Canal" : 134,
	"Zerg Hydralisk Den" : 135,
	"Zerg Defiler Mound" : 136,
	"Zerg Greater Spire" : 137,
	"Zerg Queen's Nest" : 138,
	"Zerg Evolution Chamber" : 139,
	"Zerg Ultralisk Cavern" : 140,
	"Zerg Spire" : 141,
	"Zerg Spawning Pool" : 142,
	"Zerg Creep Colony" : 143,
	"Zerg Spore Colony" : 144,
	"Unused Zerg Building1" : 145,
	"Zerg Sunken Colony" : 146,
	"Zerg Overmind (With Shell)" : 147,
	"Zerg Overmind" : 148,
	"Zerg Extractor" : 149,
	"Mature Chrysalis" : 150,
	"Zerg Cerebrate" : 151,
	"Zerg Cerebrate Daggoth" : 152,
	"Unused Zerg Building2" : 153,
	"Protoss Nexus" : 154,
	"Protoss Robotics Facility" : 155,
	"Protoss Pylon" : 156,
	"Protoss Assimilator" : 157,
	"Unused Protoss Building1" : 158,
	"Protoss Observatory" : 159,
	"Protoss Gateway" : 160,
	"Unused Protoss Building2" : 161,
	"Protoss Photon Cannon" : 162,
	"Protoss Citadel of Adun" : 163,
	"Protoss Cybernetics Core" : 164,
	"Protoss Templar Archives" : 165,
	"Protoss Forge" : 166,
	"Protoss Stargate" : 167,
	"Stasis Cell/Prison" : 168,
	"Protoss Fleet Beacon" : 169,
	"Protoss Arbiter Tribunal" : 170,
	"Protoss Robotics Support Bay" : 171,
	"Protoss Shield Battery" : 172,
	"Khaydarin Crystal Formation" : 173,
	"Protoss Temple" : 174,
	"Xel'Naga Temple" : 175,
	"Mineral Field (Type 1)" : 176,
	"Mineral Field (Type 2)" : 177,
	"Mineral Field (Type 3)" : 178,
	"Cave (Unused)" : 179,
	"Cave-in (Unused)" : 180,
	"Cantina (Unused)" : 181,
	"Mining Platform (Unused)" : 182,
	"Independent Command Center (Unused)" : 183,
	"Independent Starport (Unused)" : 184,
	"Independent Jump Gate (Unused)" : 185,
	"Ruins (Unused)" : 186,
	"Khaydarin Crystal Formation (Unused)" : 187,
	"Vespene Geyser" : 188,
	"Warp Gate" : 189,
	"Psi Disrupter" : 190,
	"Zerg Marker" : 191,
	"Terran Marker" : 192,
	"Protoss Marker" : 193,
	"Zerg Beacon" : 194,
	"Terran Beacon" : 195,
	"Protoss Beacon" : 196,
	"Zerg Flag Beacon" : 197,
	"Terran Flag Beacon" : 198,
	"Protoss Flag Beacon" : 199,
	"Power Generator" : 200,
	"Overmind Cocoon" : 201,
	"Dark Swarm" : 202,
	"Floor Missile Trap" : 203,
	"Floor Hatch (Unused)" : 204,
	"Left Upper Level Door" : 205,
	"Right Upper Level Door" : 206,
	"Left Pit Door" : 207,
	"Right Pit Door" : 208,
	"Floor Gun Trap" : 209,
	"Left Wall Missile Trap" : 210,
	"Left Wall Flame Trap" : 211,
	"Right Wall Missile Trap" : 212,
	"Right Wall Flame Trap" : 213,
	"Start Location" : 214,
	"Flag" : 215,
	"Young Chrysalis" : 216,
	"Psi Emitter" : 217,
	"Data Disc" : 218,
	"Khaydarin Crystal" : 219,
	"Mineral Cluster Type 1" : 220,
	"Mineral Cluster Type 2" : 221,
	"Protoss Vespene Gas Orb Type 1" : 222,
	"Protoss Vespene Gas Orb Type 2" : 223,
	"Zerg Vespene Gas Sac Type 1" : 224,
	"Zerg Vespene Gas Sac Type 2" : 225,
	"Terran Vespene Gas Tank Type 1" : 226,
	"Terran Vespene Gas Tank Type 2" : 227,
}


