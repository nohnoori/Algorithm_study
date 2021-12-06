function solution(lottos, win_nums) {
    const rank = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    let minRank = lottos.filter(lotto => win_nums.includes(lotto)).length;
    let maxRank = minRank + lottos.filter(lotto => lotto === 0).length;

    return [rank[maxRank], rank[minRank]];
}