#ifndef LINESEARCHINCLUDED
#define LINESEARCHINCLUDED
#include "AlgStrategy.hpp"
#include "IterationData.hpp"
// #include "FatropAlg.hpp"
#include "templates/NLPAlg.hpp"
#include "solver/FatropData.hpp"
#include "solver/Filter.hpp"
#include <cmath>
namespace fatrop
{
    class LineSearch : public AlgStrategy
    {
    public:
        LineSearch(
            const RefCountPtr<FatropParams> &fatropparams,
            const RefCountPtr<FatropNLP> &nlp,
            const RefCountPtr<FatropData> &fatropdata) : AlgStrategy(fatropparams),
                                                         fatropnlp_(nlp),
                                                         fatropdata_(fatropdata){};
        virtual int FindAcceptableTrialPoint(double mu) = 0;
        inline int EvalCVNext()
        {
            return fatropnlp_->EvalConstraintViolation(
                fatropdata_->x_next,
                fatropdata_->s_next,
                fatropdata_->g_next);
        }
        double EvalObjNext()
        {
            double res = 0.0;
            fatropnlp_->EvalObj(
                fatropdata_->obj_scale,
                fatropdata_->x_next,
                res);
            return res;
        }
        RefCountPtr<FatropNLP> fatropnlp_;
        RefCountPtr<FatropData> fatropdata_;
    };

    class BackTrackingLineSearch : public LineSearch
    {
    public:
        BackTrackingLineSearch(
            const RefCountPtr<FatropParams> &fatropparams,
            const RefCountPtr<FatropNLP> &nlp,
            const RefCountPtr<FatropData> &fatropdata,
            const RefCountPtr<Filter> &filter,
            const RefCountPtr<Journaller> &journaller)
            : LineSearch(fatropparams, nlp, fatropdata), filter_(filter), journaller_(journaller)
        {
            Initialize();
        };
        void Initialize()
        {
            // todo avoid reallocation when maxiter doesn't change
            s_phi = fatrop_params_->s_phi;
            delta = fatrop_params_->delta;
            s_theta = fatrop_params_->s_theta;
            gamma_theta = fatrop_params_->gamma_theta;
            gamma_phi = fatrop_params_->gamma_phi;
            eta_phi = fatrop_params_->eta_phi;
        }
        int FindAcceptableTrialPoint(double mu)
        {
            double alpha_primal = 1.0;
            double alpha_dual = 1.0;
            fatropdata_->AlphaMax(alpha_primal, alpha_dual, MAX(1-mu,0.99));
            double cv_curr = fatropdata_->CVL1Curr();
            double obj_curr = fatropdata_->obj_curr;
            double barrier_curr = fatropdata_->EvalBarrierCurr(mu);
            obj_curr += barrier_curr;
            double lin_decr_curr = fatropdata_->LinDecrCurr();
            double barrier_decr_curr = fatropdata_->EvalBarrierLinDecr(mu);
            lin_decr_curr += barrier_decr_curr;
            // cout << "lindecr " << lin_decr_curr << endl;
            for (int ll = 1; ll < 50; ll++)
            {
                fatropdata_->TryStep(alpha_primal, alpha_dual);
                EvalCVNext();
                double cv_next = fatropdata_->CVL1Next();
                double obj_next = EvalObjNext();
                double barrier_next = fatropdata_->EvalBarrierNext(mu);
                obj_next += barrier_next;
                // todo change iteration number from zero to real iteration number
                (journaller_->it_curr).type = 'f';
                if (filter_->IsAcceptable(FilterData(0, obj_next, cv_next)))
                {
                    bool switch_cond = (lin_decr_curr < 0) && (alpha_primal * pow(-lin_decr_curr, s_phi) > delta * pow(cv_curr, s_theta));
                    bool armijo = obj_next - obj_curr < eta_phi * alpha_primal * lin_decr_curr;
                    if (switch_cond && (cv_curr <= fatropdata_->theta_min))
                    {
                        // f-step
                        if (armijo)
                        {
                            fatropdata_->TakeStep();
                            journaller_->it_curr.alpha_pr = alpha_primal;
                            journaller_->it_curr.alpha_du = alpha_dual;
                            return ll;
                        }
                    }
                    else
                    {
                        // h-step
                        // check sufficient decrease wrt current iterate
                        if ((cv_next < (1.0 - gamma_theta) * cv_curr) || (obj_next < obj_curr - gamma_phi * cv_curr))
                        {
                            if (!switch_cond || !(armijo))
                            {
                                filter_->Augment(FilterData(0, obj_curr - gamma_phi * cv_curr, cv_curr * (1 - gamma_theta)));
                                (journaller_->it_curr).type = 'h';
                            }
                            fatropdata_->TakeStep();
                            journaller_->it_curr.alpha_pr = alpha_primal;
                            journaller_->it_curr.alpha_du = alpha_dual;
                            return ll;
                        }
                    }
                }
                alpha_primal /= 2.0;
            }
            assert(false);
            return 0;
        };
        RefCountPtr<Filter> filter_;
        RefCountPtr<Journaller> journaller_;
        double s_phi;
        double delta;
        double s_theta;
        double gamma_theta;
        double gamma_phi;
        double eta_phi;
    };
} // namespace fatrop
#endif // LINESEARCHINCLUDED