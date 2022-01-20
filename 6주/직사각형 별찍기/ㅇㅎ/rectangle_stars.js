//최대 49.27ms
process.stdin.setEncoding('utf8');
process.stdin.on('data', data => {
    let [n, m] = data.split(' ');
    console.log(("*".repeat(n) + "\n").repeat(m));
});
