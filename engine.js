// Bracket Math engine - tournament counting arithmetic.
// Mirrored by oracle.py; keep the op order identical.

function _int(x, lo, msg) {
  if (!isFinite(x) || x % 1 !== 0 || x < lo) throw new Error(msg);
  return x;
}

function _teams(n) {
  _int(n, 2, "teams must be a whole number, 2 or more");
  if (n > 1024) throw new Error("keep teams at 1024 or fewer");
}

function _s(n, one, many) {
  return n === 1 ? one : many;
}

function _p2(n) {
  return (n < 10 ? "0" : "") + n;
}

function _dur(m) {
  if (m < 60) return m + " min";
  var h = Math.floor(m / 60), r = m % 60;
  return r === 0 ? h + " h" : h + " h " + _p2(r) + " min";
}

// The bracket truth: single elimination counts.
function bracketTruth(teams) {
  _teams(teams);
  var size = 1, rounds = 0;
  while (size < teams) { size = size * 2; rounds = rounds + 1; }
  var byes = size - teams;
  var firstGames = teams - size / 2;
  return teams + " teams: bracket of " + size + ", " + byes + " " + _s(byes, "bye", "byes") + ", " +
    firstGames + " first-round " + _s(firstGames, "game", "games") + ", " + rounds + " " + _s(rounds, "round", "rounds") +
    ", " + (teams - 1) + " " + _s(teams - 1, "game", "games") + " in all.";
}

// The league truth: round robin counts.
function leagueTruth(teams, times) {
  _teams(teams);
  _int(times, 1, "times played must be a whole number, 1 or more");
  if (times > 6) throw new Error("keep times played at 6 or fewer");
  var games = times * (teams * (teams - 1) / 2);
  var perRound = Math.floor(teams / 2);
  var odd = teams % 2 === 1;
  var rounds = times * (odd ? teams : teams - 1);
  var each = times * (teams - 1);
  var how = times === 1 ? "once" : times === 2 ? "twice" : times + " times";
  var tail = odd
    ? "each team plays " + each + " and sits out " + times + " " + _s(times, "round", "rounds")
    : "every team plays " + each;
  return teams + " teams, played " + how + ": " + games + " " + _s(games, "game", "games") + " over " + rounds + " " +
    _s(rounds, "round", "rounds") + ", " + perRound + " " + _s(perRound, "game", "games") + " per round, " + tail + ".";
}

// The clock truth: owner-entered courts and game length against a game count.
function clockTruth(games, courts, minutes) {
  _int(games, 1, "games must be a whole number, 1 or more");
  _int(courts, 1, "courts must be a whole number, 1 or more");
  _int(minutes, 1, "minutes per game must be a whole number, 1 or more");
  var slots = Math.ceil(games / courts);
  return games + " " + _s(games, "game", "games") + " on " + courts + " " + _s(courts, "court", "courts") + " at " +
    minutes + " min each: " + slots + " " + _s(slots, "time slot", "time slots") + ", " + _dur(slots * minutes) + " of play.";
}
