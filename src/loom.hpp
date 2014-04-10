#include "common.hpp"
#include "cross_cat.hpp"
#include "assignments.hpp"
#include "annealing_schedule.hpp"

namespace loom
{

class Loom : noncopyable
{
public:

    Loom (
            rng_t & rng,
            const char * model_in,
            const char * groups_in = nullptr,
            const char * assign_in = nullptr);

    void dump (
            const char * groups_out = nullptr,
            const char * assign_out = nullptr);

    void infer_single_pass (
            rng_t & rng,
            const char * rows_in,
            const char * assign_out = nullptr);

    void infer_multi_pass (
            rng_t & rng,
            const char * rows_in,
            double extra_passes);

private:

    void add_row_noassign (
            rng_t & rng,
            const protobuf::SparseRow & row);

    void add_row (
            rng_t & rng,
            const protobuf::SparseRow & row,
            protobuf::Assignment & assignment);

    bool try_add_row (
            rng_t & rng,
            const protobuf::SparseRow & row);

    void remove_row (
            rng_t & rng,
            const protobuf::SparseRow & row);

    CrossCat cross_cat_;
    const size_t kind_count_;
    Assignments assignments_;
    std::vector<ProductModel::Value> factors_;
    VectorFloat scores_;
};

} // namespace loom
