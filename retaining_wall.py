class RetainingWallSolver(object):
    def retaining_wall(self, wood_lengths, required_lengths):
        self.required_lengths = required_lengths
        return self.retaining_wall_recursive(wood_lengths, len(required_lengths) - 1)

    def retaining_wall_recursive(self, wood_lengths, required_length_idx):
        if required_length_idx <= -1:
            return {
                'cuts': []
            }

        current_required_length = self.required_lengths[required_length_idx]

        possible_subsolutions = []

        # only consider non duplicate wood lengths
        seen_wood_lengths = set()
        for wood_length_idx in range(len(wood_lengths) - 1, -1, -1):
            if wood_lengths[wood_length_idx] in seen_wood_lengths:
                continue
            seen_wood_lengths.add(wood_lengths[wood_length_idx])

            if wood_lengths[wood_length_idx] < current_required_length:
                # cant cut from this length
                continue

            # what if we chose to cut current_required_length out of this wood length

            wood_lengths[wood_length_idx] -= current_required_length

            subsolution = self.retaining_wall_recursive(wood_lengths, required_length_idx - 1)

            if not subsolution:
                continue

            # don't need to cut if the wood length and required length are the same
            if wood_lengths[wood_length_idx] != 0:
                subsolution['cuts'].append({
                    'wood_num': wood_length_idx,
                    'cut_amount': current_required_length
                })

            #roll back the state of wood_lengths
            wood_lengths[wood_length_idx] += current_required_length

            possible_subsolutions.append(subsolution)

        if len(possible_subsolutions) == 0:
            return False

        # return the solution with the least number of cuts
        return min(possible_subsolutions, key=lambda s: len(s['cuts']))
