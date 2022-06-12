// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract SimpleStorage {
    uint256 public favoriteNumber = 5;

    function store(uint256 _favouriteNumber) public {
        favoriteNumber = _favouriteNumber;
    }

    function retrieve() public view returns(uint256) {
        return favoriteNumber;
    }
}